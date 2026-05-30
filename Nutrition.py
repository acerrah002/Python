import json

def writetoprofile():
    userDate = input("Enter the date (YYYY-MM-DD): ")
    userBreakfastCalories = int(input("Enter calories for breakfast: "))
    userBreakfastProtein = int(input("Enter protein for breakfast: "))

    userLunchCalories = int(input("Enter calories for Lunch: "))
    userLunchProtein = int(input("Enter protein for Lunch: "))

    userDinnerCalories = int(input("Enter calories for Dinner: "))
    userDinnerProtein = int(input("Enter protein for Dinner: "))

    TotalCalories = userBreakfastCalories + userLunchCalories + userDinnerCalories
    TotalProtein = userBreakfastProtein + userLunchProtein + userDinnerProtein

    user_profile = {
        #This is in YYYY-MM-DD format
        "Date" : userDate,
        "Calories" : TotalCalories,
        #103, 70, 80
        "Protein" : TotalProtein,
        "Meals":{
                "Breakfast" : {
                "Calories" : userBreakfastCalories,
                "Protein" : userBreakfastProtein
            },

            "Lunch" : {
                "Calories" : userLunchCalories,
                "Protein" : userLunchProtein
            },

            "Dinner" : {
                "Calories" : userDinnerCalories,
                "Protein" : userDinnerProtein}
          }
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
