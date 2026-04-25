from tkinter import *
from tkinter import ttk
import keyboard
import pyautogui

listofmousepositon=[]
pyautogui.PAUSE

def printhello():
    print("Hello World")

def createclickposition():
    if keyboard.read_key()=="+":
                while not (keyboard.is_pressed('space')):
                    if keyboard.on_release('+'):
                        #listofmousepositon.append(pyautogui.position())
                        print(pyautogui.position())

root = Tk()
frm = ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm,text="Hello World!").grid(column=0,row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=0)

ttk.Label(frm,text="Add Position").grid(column=0,row=1)
ttk.Button(frm, text="Print",command=printhello).grid(column=1,row=1)

ttk.Label(frm,text="End Code").grid(column=0,row=1)
ttk.Button(frm, text="Print",command=printhello).grid(column=1,row=1)
root.mainloop()
