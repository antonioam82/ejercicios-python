#CREATING FRAMES FROM A VIDEO

#LIBRARIES YOU NEED.
import cv2
import os

#ENTER PATH TO VIDEO.
root = input("Enter path to video: ")

#READ THE VIDEO.
cam = cv2.VideoCapture(root)

#CREATE 'data' FOLDER IF IT NOT EXISTS.
try:
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('Error: Creating directory of data')

#CREATE FRAME COUNTER.
currentframe = 0

while(True):
    #READ FROM FRAMES
    ret,frame = cam.read()

    if ret:
        #IF VIDEO IS STILL LETF, CONTINUE CREATING FRAMES.
        name = './data/frame'+str(currentframe)+'.jpg'
        print('Creating...'+name)
        
        #WRITE THE EXTRACTED FRAME.
        cv2.imwrite(name,frame)
        
        #INCREASE FRAME COUNTER.
        currentframe += 1
    else:
        #FINISH THE LOOP.
        break

#FINISH THE PROGRAM.
cam.release()
cv2.destroyAllWindows()
