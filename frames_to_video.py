import cv2
import numpy as np
import os
from os.path import isfile, join


def convertToVideo(pathIn, pathOut, fps, time):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    files.sort(key=lambda x: int((x.split(".")[0]).split(" ")[1]))#REORDENA FRAMES
    for i in range(len(files)):
        filename = pathIn+files[i]
        print(filename)
        img=cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)

        for k in range (time):
            frame_array.append(img)

    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    print("TASK COMPLETED")

#EJECUTAMOS  FUNCIÓN.
directory = #RUTA A LA COLECCIÓN DE FRAMES ej:'C:/Users/Antonio/Documents/Mis programas/frames'
pathIn = directory + '/'
pathOut=pathIn + 'video.avi' 
fps = 20
time = 5
convertToVideo(pathIn, pathOut, fps, time)
