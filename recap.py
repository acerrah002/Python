#print("Hello world!")
#we are going to make rock/paper/scissors
#we will have out options to pick nested inside a while loop
#then we will have several if statements to play agasint AI
import random
choices = ["rock","paper","scissors"]
AI=random.choice(choices)

Tryagain = input("Want to play?(n/y)")
while Tryagain != "n":
    user = input("Type what you'll do: (Rock,Paper,Scissor) ")
    user = user.lower()
    #print(user)
    choices = ["rock","paper","scissors"]
    AI=random.choice(choices)

    if user == "scissor":
        if AI == "rock":
            print("AI Won")
        elif AI == "paper":
            print("User Won")
        else:
            print("Draw")

    elif user == "paper":
        if AI == "rock":
            print("User Won")
        elif AI == "paper":
            print("Draw")
        else:
            print("AI Won")

    else:
        if AI == "rock":
            print("Draw")
        elif AI == "paper":
            print("AI Won")
        else:
            print("User Won")
    Tryagain = input("Want to play?(n/y)")
