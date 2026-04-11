import keyboard
import pyautogui

print("code started")
while True:
    if keyboard.read_key()=="right":
        pyautogui.write("Hello world!")
        userx , usery = pyautogui.position()
        print(userx, usery)
        while True: 
            pyautogui.moveTo(userx, usery)
            pyautogui.click()
    elif keyboard.read_key()=="up":
        break
