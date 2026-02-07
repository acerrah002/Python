import random


#This is a comment , they are used to communicate with dev without
#affecting code
HeroName = "23"
ClassHero = "Assassin"
Age = 51

StartLocation = "Tavern of Dragons"
StarterNPC = "TravernBartender"

#print(StarterNPC,":","Welcome,",HeroName)
#inputUser = input("Would you like to go on a quest?: ")

#print(inputUser)

#print("You've been kicked out")

#Forestname = "Enchanted Forest"

##print(HeroName, "Has decided to go to a foreest", Forestname)

#This is a Boolean with is equal to True or False
#Boolean = True

#if Boolean == True:
    #print("Yummy")
#else:
    #print("You did no eat the mushroom!")

#print("You start feeling dizzy...")
#print("You wake up in a strange place...")

StrangePlace = "Goblin Terrority"
GoblinName = "Bob the Goblin"

#print(GoblinName,":", "You've been taken prisoner for stepping foot in our forest >:( ")

#float is any number with a decimal
CaptureMoney = 24.5
#print(GoblinName,":", "You must pay, $", CaptureMoney)

UserMoney = 100.0

#print("You have paid the goblin $", CaptureMoney)
UserMoney = UserMoney - CaptureMoney
#print("You now have $", UserMoney)
#print("THE GOBBLIN TERRORITY IS UNDER ATTACK BY FOREST ELVES!!!")
UserHealth = 100

#print("You've been hit with an arrow!!!!")
UserHealth = UserHealth - 10

#print("You see Bob napping forever...")

StealBoolean = True

RandomInt = random.randint(1,3)

if StealBoolean == True:
    #print("You steal from Bobs pockets")
    #$533.5
    #Money got destroyed ge only had $2
    #$50
    #Nesting a if statement
    if RandomInt == 1:
        #print("You found $50!")
        UserMoney = UserMoney + 50

    elif RandomInt == 2:
        #print("You found $2!")
        UserMoney = UserMoney + 2

    elif RandomInt == 3:
        #print("You found $533.5!")
        UserMoney = UserMoney + 533.5
    else:
        #print("You found nothing... Matter of fact you dropped some money...")
        
        UserMoney = UserMoney - 20

#UserMoney = 609.0
#Jayden has $50
#Quicy has $125.5
UserMoney = (609.0 + 50 + 125.5)/3

print("You now have $", UserMoney)

print("You secretly hid inside a elf carrage")
print("And coincidently this was the elf generals carrage")

CarrageRandom = random.randint(1,2)

if CarrageRandom == 1:
    print("The Elf General finds you and notices you were a prisoner to the Goblins")
    print("He asks you where you'd like to go at a price, since you've already entered the carrage")
    #Room for more
elif CarrageRandom == 2:
    print("The Elf General doesn't notice you")
    #Room for more
import random


#This is a comment , they are used to communicate with dev without
#affecting code
HeroName = "23"
ClassHero = "Assassin"
Age = 51

StartLocation = "Tavern of Dragons"
StarterNPC = "TravernBartender"

#print(StarterNPC,":","Welcome,",HeroName)
#inputUser = input("Would you like to go on a quest?: ")

#print(inputUser)

#print("You've been kicked out")

#Forestname = "Enchanted Forest"

##print(HeroName, "Has decided to go to a foreest", Forestname)

#This is a Boolean with is equal to True or False
#Boolean = True

#if Boolean == True:
    #print("Yummy")
#else:
    #print("You did no eat the mushroom!")

#print("You start feeling dizzy...")
#print("You wake up in a strange place...")

StrangePlace = "Goblin Terrority"
GoblinName = "Bob the Goblin"

#print(GoblinName,":", "You've been taken prisoner for stepping foot in our forest >:( ")

#float is any number with a decimal
CaptureMoney = 24.5
#print(GoblinName,":", "You must pay, $", CaptureMoney)

UserMoney = 100.0

#print("You have paid the goblin $", CaptureMoney)
UserMoney = UserMoney - CaptureMoney
#print("You now have $", UserMoney)
#print("THE GOBBLIN TERRORITY IS UNDER ATTACK BY FOREST ELVES!!!")
UserHealth = 100

#print("You've been hit with an arrow!!!!")
UserHealth = UserHealth - 10

#print("You see Bob napping forever...")

StealBoolean = True

RandomInt = random.randint(1,3)

if StealBoolean == True:
    #print("You steal from Bobs pockets")
    #$533.5
    #Money got destroyed ge only had $2
    #$50
    #Nesting a if statement
    if RandomInt == 1:
        #print("You found $50!")
        UserMoney = UserMoney + 50

    elif RandomInt == 2:
        #print("You found $2!")
        UserMoney = UserMoney + 2

    elif RandomInt == 3:
        #print("You found $533.5!")
        UserMoney = UserMoney + 533.5
    else:
        #print("You found nothing... Matter of fact you dropped some money...")
        
        UserMoney = UserMoney - 20

#UserMoney = 609.0
#Jayden has $50
#Quicy has $125.5
UserMoney = (609.0 + 50 + 125.5)/3

print("You now have $", UserMoney)

print("You secretly hid inside a elf carrage")
print("And coincidently this was the elf generals carrage")

CarrageRandom = random.randint(1,2)

if CarrageRandom == 1:
    print("The Elf General finds you and notices you were a prisoner to the Goblins")
    print("He asks you where you'd like to go at a price, since you've already entered the carrage")
    #Room for more
elif CarrageRandom == 2:
    print("The Elf General doesn't notice you")
    #Room for more