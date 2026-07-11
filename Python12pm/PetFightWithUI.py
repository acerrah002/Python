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
def printsHello():
    print("Hello World")
    label.configure(text="new text")


app = customtkinter.CTk()
app.geometry("800x800")

button = customtkinter.CTkButton(app, text="Attack", command=printsHello)
button2 = customtkinter.CTkButton(app, text="Defend", command=printsHello)

label = customtkinter.CTkLabel(app, text="NOTHING")
HealthLabel = customtkinter.CTkLabel(app, text="Health: 100")
PetLabel = customtkinter.CTkLabel(app,text=pet)

HealthLabel.pack(padx=0, pady=20)
PetLabel.pack(padx=10, pady=20)
label.pack(padx=20, pady=20)
button.pack(padx=30, pady=20)
button2.pack(padx=30, pady=40)

app.mainloop()
