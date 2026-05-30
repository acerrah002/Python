import json

def writetoprofile():
    user_profile = {
        #This is in YYYY-MM-DD format
        "Date" : "2026-05-30",
        "Calories" : 2000,
        #103, 70, 80
        "Protein" : 70,
        "Meals":{
                "Breakfast" : {
                "Calories" : 500,
                "Protein" : 20
            },

            "Lunch" : {
                "Calories" : 700,
                "Protein" : 30
            },

            "Dinner" : {
                "Calories" : 800,
                "Protein" : 20}
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
