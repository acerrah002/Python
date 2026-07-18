import customtkinter
import random
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
Health = 100

def printsHello():
    print("Hello World")
    label.configure(text="new text")

def Attack(HP, label ,MaxDamage, WhichPet):
    print("Attack")
    HP = HP - random.randint(0,MaxDamage)
    label.configure(text="Health: " + str(HP))
    print(WhichPet, " was Attcked")
    global Health
    Health = HP
    
def Defend(HP, label, MaxDefense, WhichPet):
    print("Defend")
    global Health
    Health = Health + random.randint(0,MaxDefense)
    HealthLabel.configure(text="Health: " + str(Health))
    print(WhichPet, " was Defended")

def ShowAttackScreen(pet,enemy):
    #Packs Position where our UI will be
    HealthLabel.pack(padx=0, pady=20)
    PetLabel.pack(padx=10, pady=20)
    #show our pets on attack screen
    PetLabel.configure(text=pet)
    EnemyLabel.configure(text=enemy)
    EnemyLabel.pack(padx=20, pady=20)
    button.pack(padx=30, pady=20)
    button2.pack(padx=30, pady=40)

def HideMainScreen():
    print("Main Screen Hiden")
    #Exmaple
    PetText.pack_forget()
    EnemyText.pack_forget()
    SubmitPets.pack_forget()
    ShowAttackScreen(PetText.get("0.0", "end"), EnemyText.get("0.0", "end"))


def ShowMainScreen():
    pass


app = customtkinter.CTk()
app.geometry("800x800")
#Labels
EnemyLabel = customtkinter.CTkLabel(app, text="NOTHING")
HealthLabel = customtkinter.CTkLabel(app, text="Health: 100")
PetLabel = customtkinter.CTkLabel(app,text=pet)
#Buttons
button = customtkinter.CTkButton(app, text="Attack", command=lambda: Attack(Health, HealthLabel, 10, "1"))
button2 = customtkinter.CTkButton(app, text="Defend", command=lambda: Defend(Health, HealthLabel, 10, "1"))
#TextBox
PetText = customtkinter.CTkTextbox(app)
EnemyText = customtkinter.CTkTextbox(app)
SubmitPets = customtkinter.CTkButton(app, text="Submit Pets", command=lambda: HideMainScreen())
#Pack TextBox
PetText.pack(padx=20, pady=20)
EnemyText.pack(padx=20, pady=40)
SubmitPets.pack(padx=20, pady=60)
#Runs Application
app.mainloop()
