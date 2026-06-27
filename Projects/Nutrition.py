import json
import os
import customtkinter as ctk 


#Main Application controller
class NutritionApp(ctk.CTk):
     def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Nutrition Tracker")
        self.grid_columnconfigure(0,weight=1)

        self.current_frame = None
        self.show_frame(MainMenu)

     def show_frame(self, frame_class):
        """Destroys the old screen frame and loads the new one."""
        if self.current_frame is not None:
            self.current_frame.destroy()
            
        # Initialize the new frame, passing 'self' (this window) as the master
        self.current_frame = frame_class(master=self)
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


#Main screen
class MainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master) # 'master' is the NutritionApp window
        self.grid_columnconfigure(0, weight=1)
        
        button1 = ctk.CTkButton(self, text="Calendar",
                                command=lambda: master.show_frame(Calender))
        
        # NOW 'master' works perfectly because it was passed into __init__
        button2 = ctk.CTkButton(self, text="Track Nutrition", 
                                command=lambda: master.show_frame(TrackNutrition))
        
        button1.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)
        button2.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

#Tracker Page
class TrackNutrition(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)
        #Title
        Label = ctk.CTkLabel(self, text="Track Nutrition")
        Label.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=10)
        #Date input
        Labe2 = ctk.CTkLabel(self, text="Enter Date")
        Labe2.grid(row=1, column=0, sticky="w", padx=20, pady=10)
        entry = ctk.CTkEntry(self, placeholder_text="Enter Date (YYYY-MM-DD)")
        entry.grid(row=1, column=1, sticky="ew", padx=20, pady=10)
        #TitleBreakfast
        BreakFastLabel = ctk.CTkLabel(self, text="Enter Breakfast Nutrition")
        BreakFastLabel.grid(row=2, column=0, columnspan=2, sticky="w", padx=20, pady=10)
        #Breakfast Calories
        BreakfastCaloriesLabel = ctk.CTkLabel(self, text="Calories")
        BreakfastCaloriesLabel.grid(row=3, column=0, sticky="w", padx=20, pady=10)

#Calender Page
class Calender(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)
        #Title
        Label = ctk.CTkLabel(self, text="Calender")
        Label.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=10)
        #Date input
        

#functions for later use
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
    
#we want to organize the dates in a weekly order
#make a simple UI using Tkinker to select the days as one of the number in the weeks
#then wehn you click it shows the total protein, total calories, and the meals for that day
#also shows the 3 meals and how much calories and protein for each meal

#user = input("Do you want to write to the profile or read from it? (write/read)(1/2): ")
#if user == "1":
#    writetoprofile()
#elif user == "2":
#    readfromprofile()

if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop()
