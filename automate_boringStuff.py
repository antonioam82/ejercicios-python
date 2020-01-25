import pyautogui
import time

#pyautogui.moveTo(558, 899)
#time.sleep(1)
#pyautogui.click()
#time.sleep(1)
#pyautogui.moveTo(696, 135)
#time.sleep(1)
#pyautogui.doubleClick()
#time.sleep(1)
#pyautogui.moveTo(214, 427)
#time.sleep(1)
#pyautogui.doubleClick() 

#distance = 200
#while distance > 0:
    #pyautogui.drag(distance, 0, duration=0.25)
    #distance -= 5
    #pyautogui.drag(0, distance, duration=0.25)
    #pyautogui.drag(-distance, 0, duration=0.25)
    #distance -= 5
    #pyautogui.drag(0, -distance, duration=0.25)#

#DELETING FILES FROM "Python" FOLDER.
for i in range(0,149):
    pyautogui.moveTo(219,146)
    time.sleep(0.2)
    pyautogui.click(button='right')
    time.sleep(0.2)
    pyautogui.moveTo(253,682)
    time.sleep(0.2)
    pyautogui.click()
