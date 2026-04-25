import keyboard
import pyautogui
import time
#Defined a list
listofmousepositon=[]
#We fixed a pyautogui setting so we can click faster
pyautogui.PAUSE
#Debug print
print("code started")
#Input to choose what to do
user = input("what would you like to do?(1,2)")
#Function to move and click at a position
def moveandclickfunc(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click()
#This is section to add to a list or click them
if user == "1":
    #this add to the list
    if keyboard.read_key()=="right":
                print("keyboard recognized")
                cooldown = False
                while not (keyboard.is_pressed('space')):
                    if keyboard.is_pressed('right'):
                        if not cooldown:
                            print(pyautogui.position())
                            cooldown = True
                    else:
                        cooldown = False
                    time.sleep(0.01)
                    
                        
    #this removes the last position
    if keyboard.read_key()=="left" and len(listofmousepositon)>0:
                listofmousepositon.pop()

    if keyboard.read_key()=="space":
        while not (keyboard.is_pressed('right')):
            for i in range(10):
                moveandclickfunc(listofmousepositon)

elif user == "2":
    if keyboard.read_key()=="space":
        print(pyautogui.position())
print("ended code")
#Point(x=1102, y=497) cookie
#Point(x=1746, y=421) grandma
