from tkinter import *
from tkinter import ttk
import keyboard
import pyautogui

listofmousepositon=[]
pyautogui.PAUSE

def printhello():
    print("Hello World")

def createclickposition():
    print("code started")
    if keyboard.read_key()=="right":
                print("keyboard recognized")
                #click on the screen repeatedly
                while not (keyboard.is_pressed('space')):
                    #we want to check if the user pressed the button
                    #and only once will the position be shown
                    cooldown = True
                    if keyboard.on_release('+') and cooldown:
                        cooldown = False
                        #listofmousepositon.append(pyautogui.position())
                        print(pyautogui.position())
                        
                        cooldown = True

root = Tk()
frm = ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm,text="Hello World!").grid(column=0,row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)

ttk.Label(frm,text="Add Position").grid(column=0,row=1)
ttk.Button(frm, text="Print",command=createclickposition).grid(column=1,row=1)

#ttk.Label(frm,text="End Code").grid(column=0,row=1)
#ttk.Button(frm, text="Print",command=printhello).grid(column=1,row=1)
root.mainloop()
