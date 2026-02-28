import random


#This is a comment , they are used to communicate with dev without
#affecting code
HeroName = "23"
ClassHero = "Assassin"
Age = 51

StartLocation = "Tavern of Dragons"
StarterNPC = "TravernBartender"

#print(StarterNPC,": Welcome traveller",HeroName)

#print(StarterNPC,":","Welcome,",HeroName)
#inputUser = input("Would you like to go on a quest?: ")

#print(inputUser)

#print("You've been kicked out")

Forestname = "Enchanted Forest"

#print(HeroName, "Has decided to go to go deeper in the forest", Forestname)

#This is a Boolean with is equal to True or False
#Boolean = input("Would you like to eat the first mushroom we see?: ")
#Boolean = True

#if Boolean == "True":
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


UserMoney = UserMoney - CaptureMoney
#print("You have paid the goblin $", CaptureMoney)
#print("You now have $", UserMoney)

#print("THE GOBBLIN TERRORITY IS UNDER ATTACK BY FOREST ELVES!!!")
UserHealth = 100

#print("You've been hit with an arrow!!!!")
UserHealth = UserHealth - 10

#print("You see Bob napping forever...")

StealBoolean = True

RandomInt = random.randint(1,4)

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

#print("You now have $", UserMoney)

#print("You secretly hid inside a elf carrage")
#print("And coincidently this was the elf generals carrage")

CarrageRandom = random.randint(1,2)

if CarrageRandom == 1:
    print("The Elf General finds you and notices you were a prisoner to the Goblins")
    print("He asks you where you'd like to go at a price, since you've already entered the carrage")

    #Room for more
elif CarrageRandom == 2:
    print("The Elf General doesn't notice you")
    #Room for more

#List carry multiple values
locationOptions = ["Elf City",StartLocation,"SandyShores","FrozenMoutainRange"]
#this will decided where our campaign continues in the carriage
choose = random.randint(0,3)
#outputs our travel location
#print(locationOptions[choose])
#This is a variable for the trip cost
#carriagecost=(choose*50)
#this updates our money
#UserMoney=UserMoney-carriagecost

UserMoney = 261.5
#print(UserMoney)
#Loop is a condition that repeats

#while(i <= 5)
#for(i <= HeroName)

#i=0

# <= Less or Equal to
# == Same values
# >= More or Equal to
# -- deincrementing
# ++ incrementing
# += incrementing a variable to a another variable
# -= deincrementing a variable to another variable

#while(i < 5):
    #print(i)
    #i += 4

#print("You've arrived in Elf City!")
#print("it was for free")

LocationTwo = "Elf City"
#print("You've unlocked the shop")

#Functions in python are blocks that can be used multiple times
#to make a function in python we start by typing "def"



UserInput = "Nothing"


def Shop1(UserInput):
    WeaponShopPrices = {"Sharp_Katana":100,"Durable_Bow":75,"Arrow_X30":60, "The_Sky_Splitter":10000}
    #We want to keep the multiple values with the same keys
    WeaponShopItems = ["Sharp_Katana","Durable_Bow","Arrow_X30","Arrow_X30","The_Sky_Splitter"]
    PlayerWeapons = []
    while UserInput != "n":
        UserInput = input("Would you like to buy a weapon? (y/n)")
        print ("You have $",UserMoney," in weapons.")
        print("These are inventory",WeaponShopItems)
        print("These are prices",WeaponShopPrices)
        print("You have $",UserMoney," in weapons.")
        BuyUser = input("What would you like to buy?")
        if WeaponShopItems:
            #WeaponShopPrices[BuyUser]
            try:
                PlayerWeapons.append(BuyUser)
                WeaponShopItems.remove(BuyUser)
                print(WeaponShopItems)
            except:
                print("That's not a item")
        elif UserInput != "n":
            print("You exited the shop")
            break
        else:
            print("You have no more weapons to buy.")
            break
        
Shop1(UserInput)
print("Shop exitted")

#print(ShopUI())

#print(UserMoney)
#print(UserHealth)
#Considering Daggers
