import json
import os
import customtkinter as ctk

# Set the theme and color
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NutritionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Nutrition Tracker")
        self.geometry("500x550")
        
        # Configure root grid layout (1 row, 1 column for the main frame container)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Dictionary to hold the different page frames
        self.frames = {}
        
        # Initialize all pages and stack them in the same grid space
        for PageClass in (MainMenuPage, TrackNutritionPage, CalendarPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=self, controller=self)
            self.frames[page_name] = frame
            # Grid them all on top of each other
            frame.grid(row=0, column=0, sticky="nsew")
            
        # Start by showing the Main Menu
        self.show_frame("MainMenuPage")
        
    def show_frame(self, page_name):
        """Brings the requested frame to the front."""
        frame = self.frames[page_name]
        
        # If the calendar page is opened, update its display with the newest data
        if page_name == "CalendarPage":
            frame.load_and_display_data()
            
        frame.tkraise()

# ==========================================
# 1. MAIN MENU PAGE
# ==========================================
class MainMenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Configure Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # Title Label
        title_label = ctk.CTkLabel(self, text="Nutrition Tracker Menu", font=ctk.CTkFont(size=24, weight="bold"))
        title_label.grid(row=0, column=0, pady=20)
        
        # Navigation Buttons
        button1 = ctk.CTkButton(
            self, text="Open Calendar / History", font=ctk.CTkFont(size=16),
            command=lambda: controller.show_frame("CalendarPage")
        )
        button1.grid(row=1, column=0, sticky="ew", padx=40, pady=15)
        
        button2 = ctk.CTkButton(
            self, text="Track New Nutrition Entry", font=ctk.CTkFont(size=16),
            command=lambda: controller.show_frame("TrackNutritionPage")
        )
        button2.grid(row=2, column=0, sticky="ew", padx=40, pady=15)

# ==========================================
# 2. TRACK NUTRITION PAGE (Form Input)
# ==========================================
class TrackNutritionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.grid_columnconfigure((0, 1), weight=1)
        
        # Title
        title = ctk.CTkLabel(self, text="Track Nutrition", font=ctk.CTkFont(size=20, weight="bold"))
        title.grid(row=0, column=0, columnspan=2, pady=15)
        
        # Date Entry
        ctk.CTkLabel(self, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.date_entry = ctk.CTkEntry(self, placeholder_text="e.g., 2026-06-13")
        self.date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        # Create Input Fields dynamically for Meals
        self.meal_inputs = {}
        meals = ["Breakfast", "Lunch", "Dinner"]
        
        current_row = 2
        for meal in meals:
            # Section Header
            lbl = ctk.CTkLabel(self, text=f"--- {meal} ---", font=ctk.CTkFont(weight="bold"))
            lbl.grid(row=current_row, column=0, columnspan=2, pady=(10, 2))
            current_row += 1
            
            # Calories Entry
            ctk.CTkLabel(self, text="Calories:").grid(row=current_row, column=0, padx=10, pady=2, sticky="e")
            cal_ent = ctk.CTkEntry(self, placeholder_text="kcal")
            cal_ent.grid(row=current_row, column=1, padx=10, pady=2, sticky="w")
            current_row += 1
            
            # Protein Entry
            ctk.CTkLabel(self, text="Protein (g):").grid(row=current_row, column=0, padx=10, pady=2, sticky="e")
            prot_ent = ctk.CTkEntry(self, placeholder_text="grams")
            prot_ent.grid(row=current_row, column=1, padx=10, pady=2, sticky="w")
            current_row += 1
            
            # Save references to extract data later
            self.meal_inputs[meal] = {"Calories": cal_ent, "Protein": prot_ent}
            
        # Status Message Label
        self.status_label = ctk.CTkLabel(self, text="", text_color="green")
        self.status_label.grid(row=current_row, column=0, columnspan=2, pady=5)
        current_row += 1
        
        # Control Buttons
        save_btn = ctk.CTkButton(self, text="Save Entry", fg_color="green", hover_color="darkgreen", command=self.save_data)
        save_btn.grid(row=current_row, column=0, padx=10, pady=15)
        
        back_btn = ctk.CTkButton(self, text="Back to Menu", command=lambda: controller.show_frame("MainMenuPage"))
        back_btn.grid(row=current_row, column=1, padx=10, pady=15)

    def save_data(self):
        date_str = self.date_entry.get().strip()
        if not date_str:
            self.status_label.configure(text="Error: Date field is required!", text_color="red")
            return
            
        meals_data = {}
        try:
            for meal, entries in self.meal_inputs.items():
                # Fallback to 0 if inputs are left blank
                cal = int(entries["Calories"].get() or 0)
                prot = int(entries["Protein"].get() or 0)
                meals_data[meal] = {"Calories": cal, "Protein": prot}
        except ValueError:
            self.status_label.configure(text="Error: Please enter numbers for macros!", text_color="red")
            return
            
        total_calories = sum(info["Calories"] for info in meals_data.values())
        total_protein = sum(info["Protein"] for info in meals_data.values())
        
        # Load profile
        filename = "user_profile.json"
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r") as file:
                user_profile = json.load(file)
        else:
            user_profile = {}
            
        # Save structured data exactly format-matching your original file blueprint
        user_profile[date_str] = {
            "TotalCalories": total_calories,
            "TotalProtein": total_protein,
            "Meals": meals_data
        }
        
        with open(filename, "w") as file:
            json.dump(user_profile, file, indent=4)
            
        self.status_label.configure(text="Log Successfully Saved!", text_color="green")
        self.clear_fields()

    def clear_fields(self):
        self.date_entry.delete(0, 'end')
        for entries in self.meal_inputs.values():
            entries["Calories"].delete(0, 'end')
            entries["Protein"].delete(0, 'end')

# ==========================================
# 3. CALENDAR / HISTORY VIEW PAGE
# ==========================================
class CalendarPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.grid_columnconfigure(0, weight=1)
        
        title = ctk.CTkLabel(self, text="Logged Dates History", font=ctk.CTkFont(size=20, weight="bold"))
        title.grid(row=0, column=0, pady=10)
        
        # Dropdown menu to pick a saved date
        self.date_dropdown = ctk.CTkOptionMenu(self, values=[], command=self.display_date_details)
        self.date_dropdown.grid(row=1, column=0, pady=10)
        self.date_dropdown.set("Select a Date")
        
        # Textbox displaying the formatted logs
        self.display_box = ctk.CTkTextbox(self, width=400, height=280, font=ctk.CTkFont(size=13))
        self.display_box.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        
        back_btn = ctk.CTkButton(self, text="Back to Menu", command=lambda: controller.show_frame("MainMenuPage"))
        back_btn.grid(row=3, column=0, pady=15)
        
        self.profile_data = {}

    def load_and_display_data(self):
        """Loads entries dynamically into the dropdown menu configuration."""
        filename = "user_profile.json"
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "r") as file:
                self.profile_data = json.load(file)
                
            dates = list(self.profile_data.keys())
            sorted_dates = sorted(dates, reverse=True) # Shows newest dates first
            
            if sorted_dates:
                self.date_dropdown.configure(values=sorted_dates)
                self.date_dropdown.set(sorted_dates[0])
                self.display_date_details(sorted_dates[0])
            else:
                self.no_data_state()
        else:
            self.no_data_state()

    def no_data_state(self):
        self.date_dropdown.configure(values=[])
        self.date_dropdown.set("No saved records found")
        self.display_box.delete("1.0", "end")
        self.display_box.insert("1.0", "Please record nutrition logs from the main menu first.")

    def display_date_details(self, selected_date):
        """Formats and presents JSON macro metrics into the textual display box."""
        if not self.profile_data or selected_date not in self.profile_data:
            return
            
        day_info = self.profile_data[selected_date]
        
        # Quick fix to prevent nesting errors if files were saved via old structure
        if selected_date in day_info: 
            day_info = day_info[selected_date]
            
        self.display_box.delete("1.0", "end")
        
        # Build clean string formatting out of user's JSON file 
        output_str = f"Date Summary: {selected_date}\n"
        output_str += "="*40 + "\n"
        output_str += f"Total Daily Calories : {day_info.get('TotalCalories', 0)} kcal\n"
        output_str += f"Total Daily Protein  : {day_info.get('TotalProtein', 0)} g\n"
        output_str += "="*40 + "\n\n"
        
        meals = day_info.get("Meals", {})
        for meal, macros in meals.items():
            output_str += f"• {meal}:\n"
            output_str += f"  - Calories: {macros.get('Calories', 0)} kcal\n"
            output_str += f"  - Protein : {macros.get('Protein', 0)} g\n\n"
            
        self.display_box.insert("1.0", output_str)

# ==========================================
# APP EXECUTION START
# ==========================================
if __name__ == "__main__":
    app = NutritionApp()
    app.mainloop()
