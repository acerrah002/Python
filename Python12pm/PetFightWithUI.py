import customtkinter
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

def Attack(HP, label):
    print("Attack")
    HP = HP - 10
    label.configure(text="Health: " + str(HP))
    print("Pet was Attcked")
    global Health
    Health = HP

def Defend(HP, label):
    print("Defend")
    global Health
    Health = Health + 10
    HealthLabel.configure(text="Health: " + str(Health))
    print("Pet was Defended")

app = customtkinter.CTk()
app.geometry("800x800")
#Labels
label = customtkinter.CTkLabel(app, text="NOTHING")
HealthLabel = customtkinter.CTkLabel(app, text="Health: 100")
PetLabel = customtkinter.CTkLabel(app,text=pet)
#Buttons
button = customtkinter.CTkButton(app, text="Attack", command=lambda: Attack(Health, HealthLabel))
button2 = customtkinter.CTkButton(app, text="Defend", command=lambda: Defend(Health, HealthLabel))
#Packs Position where our UI will be
HealthLabel.pack(padx=0, pady=20)
PetLabel.pack(padx=10, pady=20)
label.pack(padx=20, pady=20)
button.pack(padx=30, pady=20)
button2.pack(padx=30, pady=40)
#Runs Application
app.mainloop()
