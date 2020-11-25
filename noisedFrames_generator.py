import random
import numpy as np
import cv2
import os

for i in range(0,34):
    img = np.zeros((900,1600,3),np.uint8)
    
    for x in range(900):
        for y in range(1600):
            img[x,y] = [random.randint(225,240),random.randint(0,256),random.randint(0,256)]#(0,256)(0,256)

    name = "ima "+str(i)+".png"
    cv2.imwrite(name,img)
    print("DONE: ",name)
print("FINISH")
