import numpy as np
import cv2
from matplotlib import pyplot as plt
#from copy import deepcopy
import os

os.chdir(r'ruta')

img=cv2.imread(archivo,1)

def click2circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(255,0,0),4)

cv2.namedWindow("IMAGEN",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("IMAGEN",click2circle)

while True:
    cv2.imshow("IMAGEN",img)
    a=cv2.waitKey(1000)
    print("2 secs")
    if a == 27: #ESC button
        print("FIN")
        break
cv2.destroyAllWindows()
