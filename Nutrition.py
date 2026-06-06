import json
import os

def askuserinput(meal):
    inputCalories = int(input(f"Enter calories for {meal}: "))
    inputProtein  = int(input(f"Enter protein for {meal}: "))
    return {"Calories" : inputCalories, "Protein" : inputProtein}

def writetoprofile():
    userDate = input("Enter the date (YYYY-MM-DD): ")
    mealNames = ["Breakfast", "Lunch", "Dinner"]
    meals = {meal: askuserinput(meal) for meal in mealNames}
    totalCalories = sum(info["Calories"] for info in meals.values())
    totalProtein = sum(info["Protein"] for info in meals.values())

    #Load existing profile if it exists, otherwise create a new one
    filename = "user_profile.json"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as file:
            user_profile = json.load(file)
    else:
        user_profile = {}
    #updates the target data    
    user_profile[userDate] = {
        userDate :{
        "TotalCalories": totalCalories,
        "TotalProtein": totalProtein,
        "Meals": meals
        }
    }

    with open("user_profile.json", "w") as file:
        json.dump(user_profile, file)

def readfromprofile():
    #make it to only see the date and calories
    with open("user_profile.json", "r") as file:
        user_profile = json.load(file)
    print(json.dumps(user_profile, indent=3))
    #print(f"Date: {user_profile['Date']}")
    #print(f"Calories: {user_profile['Calories']}")

user = input("Do you want to write to the profile or read from it? (write/read)(1/2): ")
if user == 1:
    writetoprofile()
elif user == 2:
    readfromprofile()
