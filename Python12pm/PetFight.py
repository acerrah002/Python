pet = """
    __________
    |        |
    |        |  
    |        |
   _____________
     ( ◉  ◉ )
      \ \_/ /
  _—¯—¯—¯—¯—¯—_
 /             \-----*
|   R O A R!    |-----*
 \_—_—_—_—_—_—_/
    ||     ||
   _||_   _||_
 """

Sadpet = """
    __________
    |        |
    |        |  
    |        |
   _____________
     ( ◉  ◉ )
      \  ~  /
  _—¯—¯—¯—¯—¯—_
 /             \-----*
|   R O A R!    |-----*
 \_—_—_—_—_—_—_/
    ||     ||
   _||_   _||_
 """

petFavFood = ["Fish", "Tacos", "Stegosaurus", "Space Aliens", "Exotic Butter", "singing bears","Computers"]
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
petName = "TimOfEarth"
petLastName = "Supernova"
#MartianPetName = ""
#MartianPetLastName = ""
#for i in petName:
#    if i in vowels:
#        pass
#    else:
#       MartianPetName = MartianPetName + i
#for i in petLastName:
#    if i in vowels:
#        pass
#    else:
#        MartianPetLastName = MartianPetLastName + i
#print(MartianPetName)
#print(MartianPetLastName)
#We will make a program to translate our pets name to Marish and they do not have vowels
#No A, E, I, O, U
#Make sure the letter Q is not in the name because Martians are allergic to it
#Ex if my pets name is Tim, in Marish it would be Tm
# #look at W3schools for loops python
#figure out how to print every letter of your pets name in a for loop for example
#T
#I
#M
#torches = False
#Sprinting = True
#Eating = True
#Walking = True
#Flint = True
#Steel = True
#if agent 
#if Flint == True and Steel == True:
    #print("We can make flint and steel")
#if Walking == True or Sprinting == True:
    #print("We can move in water")
#if RespawnAnchore == True and Alive == False:
    #print("We can respawn")
#for i in petName:
    #print(i)

#DRY Dont Repeat Yourself
#In minecraft the pickaxes all destroy minerals the same instead of making it from scratch everytime
#we create a pickaxe function and change the arguments

#API
def hello(fname):
    print("Hello", fname)

#hello("Bob")
#hello("Billy")

def Addition(x,y):
    return x + y

#hello(Addition(3,4))

import random
def damage(health,damagemaximum,whichpet):
    #DR stand for damageRandom
    dr = random.randint(0,damagemaximum)
    health = health - dr
    print(whichpet," attacks pet two Health:", health, "Damage:", dr)
    return health

#create the defense function
def defense(health,defensemaximum,whichpet):
    dr = random.randint(0,defensemaximum)
    health = health + dr
    print(whichpet,"defended/Healed itself for", dr)
    return health

#make a 1 in 100 chance to do inf damage / 1 000 000 000 000
def critialattack():
    pass

#We will have 6 types of pets Plant, Fire, Water, Psychic, Fairy, and Earth

def fighting(pet1, playerhealth, pet2, enemyhealth):
    while playerhealth > 0 and enemyhealth > 0:
        user = input("Choose between Attack and Defend(1/2)")
        #if user types 1 or 2 the functions used are different
        if user == "1":
            enemyhealth = damage(enemyhealth,10,"1")
        if user == "2":
            playerhealth = defense(playerhealth,20,"1")
        playerhealth = damage(playerhealth,10,"2")
    if playerhealth <= 0:
        print("Your pet lost", Sadpet)
    else:
        print("Your pet won", pet)
fighting(pet,50,pet,50)
