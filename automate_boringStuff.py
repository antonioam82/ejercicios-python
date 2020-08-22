import pyautogui
import time
from VALID import OKI, ns

#DELETING FILES FROM "Python" FOLDER.
while True:
    num =(OKI(input("Número de archivos: ")))+1
    for i in range(0,num):
        pyautogui.moveTo(241,132)
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(0.6)
        pyautogui.moveTo(274,699)
        time.sleep(0.3)
        pyautogui.click()
    conti = ns(input("¿Continuar?: "))
    if conti == "n":
        break

