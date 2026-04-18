import keyboard
import pyautogui

pyautogui.PAUSE
print("code started")
user = input("what would you like to do?(1,2)")

def moveandclickfunc(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click()

if user == "1":
    if keyboard.read_key()=="space":
        while not (keyboard.is_pressed('right')):
            for i in range(10):
                pyautogui.click()
            #moveandclickfunc(1746,421)
            #moveandclickfunc(1746,500)
            #moveandclickfunc(1102,497) 
elif user == "2":
    if keyboard.read_key()=="space":
        print(pyautogui.position())
print("ended code")
#Point(x=1102, y=497) cookie
#Point(x=1746, y=421) grandma
