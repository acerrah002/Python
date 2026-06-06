import json

def askuserinput(meal):
    inputCalories = int(input(f"Enter calories for {meal}: "))
    inputProtein  = int(input(f"Enter protein for {meal}: "))
    return {"Calories" : inputCalories, "Protein" : inputProtein}

def writetoprofile():
    userDate = input("Enter the date (YYYY-MM-DD): ")
    #We need to reduce the repetiion of our code -----------------------------
    mealNames = ["Breakfast", "Lunch", "Dinner"]

    meals = {meal: askuserinput(meal) for meal in mealNames}
    #-------------------------------------------------------------------------
    totalCalories = sum(info["Calories"] for info in meals.values())
    totalProtein = sum(info["Protein"] for info in meals.values())
    

    user_profile = {
        "Date": userDate,
        "Calories": totalCalories,
        "Protein": totalProtein,
        "Meals": meals
        }
        

    with open("user_profile.json", "w") as file:
        json.dump(user_profile, file)

def readfromprofile():
    #make it to only see the date and calories
    with open("user_profile.json", "r") as file:
        user_profile = json.load(file)
    print(f"Date: {user_profile['Date']}")
    print(f"Calories: {user_profile['Calories']}")

writetoprofile()
