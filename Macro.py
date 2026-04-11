import keyboard
import pyautogui

print("code started")
while True:
    pyautogui.PAUSE = 0.1
    if keyboard.read_key()=="right":
        pyautogui.write("Hello world!")
        userx , usery = pyautogui.position()
        print(userx, usery)
        while True: 
            pyautogui.moveTo(userx, usery)
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            if keyboard.read_key()=="up":
                print("ended code")
                break
    elif keyboard.read_key()=="up":
        print("ended code")
        break
