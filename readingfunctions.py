import random

def get_player_choice():
    """Gets and validates the player's action choice."""
    while True:
        choice = input("\nChoose your action -- [1] Attack, [2] Heal, [3] Defend: ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice! Please enter 1, 2, or 3.")
        
def player_attack(player, enemy):
    """Calculates player attack with a chance for a critical hit or a miss."""
    hit_chance = random.random()
    if hit_chance < 0.15:
        print("\nYour attack missed completely!")
        return
    # Base damage with some randomness
    damage = random.randint(player['min_atk'], player['max_atk'])
    # 20% chance for a critical hit (1.5x damage)
    if random.random() < 0.20:
        damage = int(damage * 1.5)
        print(f"\nCRITICAL HIT! You strike the enemy for {damage} damage!")
    else:
        print(f"\nYou attack the enemy for {damage} damage.")
    enemy['hp'] -= damage
    if enemy['hp'] < 0:
        enemy['hp'] = 0

def player_heal(player):
    """Heals the player for a random amount, capped at max HP."""
    heal_amount = random.randint(12, 25)
    player['hp'] += heal_amount
    if player['hp'] > player['max_hp']:
        player['hp'] = player['max_hp']
    print(f"\nYou bandage your wounds and recover {heal_amount} HP!")

def enemy_turn(player, enemy, defending):
    """Handles the enemy's turn with a chance to attack or skip (rest)."""
    # Enemy has a small chance to hesitate/rest
    if random.random() < 0.10:
        print(f"\nThe {enemy['name']} hesitates and misses its turn!")
        return

    damage = random.randint(enemy['min_atk'], enemy['max_atk'])
    # If the player chose to defend, reduce incoming damage by 50%
    if defending:
        damage = max(1, damage // 2)
        print(f"\nYou brace yourself! The {enemy['name']}'s attack is weakened.")
    player['hp'] -= damage
    if player['hp'] < 0:
        player['hp'] = 0
        
    print(f"The {enemy['name']} attacks you for {damage} damage!")
def display_status(player, enemy):
    """Displays current HP stats for both combatants."""
    print("-" * 35)
    print(f"Your HP: {player['hp']}/{player['max_hp']}")
    print(f"{enemy['name']} HP: {enemy['hp']}/{enemy['max_hp']}")
    print("-" * 35)

def battle():
    """Main game loop managing the turn-based fight."""
    player = {'hp': 100, 'max_hp': 100, 'min_atk': 12, 'max_atk': 22}
    enemy = {'name': 'Goblin Brute', 'hp': 80, 'max_hp': 80, 'min_atk': 8, 'max_atk': 18}
    print("=== CHANCE COMBAT ARENA ===")
    print(f"A wild {enemy['name']} appears! Defeat it to win.")
    round_num = 1
    while player['hp'] > 0 and enemy['hp'] > 0:
        print(f"\n--- ROUND {round_num} ---")
        display_status(player, enemy)
        choice = get_player_choice()
        defending = False
        # Player Action Phase
        if choice == 1:
            player_attack(player, enemy)
        elif choice == 2:
            player_heal(player)
        elif choice == 3:
            defending = True
            print("\nYou take a defensive stance, preparing to block incoming damage.")
        # Check if enemy was defeated
        if enemy['hp'] <= 0:
            print(f"\nVictory! You have defeated the {enemy['name']}!")
            break
        # Enemy Turn Phase
        enemy_turn(player, enemy, defending)
        # Check if player was defeated
        if player['hp'] <= 0:
            print(f"\nDefeat... You were slain by the {enemy['name']}.")
            break
        round_num += 1
if __name__ == "__main__":
    battle()
