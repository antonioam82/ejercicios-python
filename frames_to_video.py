import cv2
import numpy as np
import os
from os.path import isfile, join


def convertToVideo(pathIn, pathOut, fps, time):
    # converts images to video
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    files.sort(key=lambda x: int((x.split(".")[0]).split(" ")[1]))
    print(files)
    for i in range(len(files)):
        filename = pathIn+files[i]
        print(filename)
        img=cv2.imread(filename)
        #img=cv2.resize(img,3840 , 2160) #make it not stretch
        height, width, layers = img.shape
        size = (width,height)#layers)

        for k in range (time):
            frame_array.append(img)

    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    print("OK")

directory = #path to images sequence
pathIn = directory + '/'
pathOut=pathIn + 'video.avi'
fps = 60
time = 5
convertToVideo(pathIn, pathOut, fps, time)
