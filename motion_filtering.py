import cv2 as cv

video = cv.VideoCapture("video1.avi")
subtractor = cv.createBackgroundSubtractorMOG2(300, 100)

while True:

    ret,frame = video.read()
    

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        if cv.waitKey(5) == ord('x'):
            break
    else:
        video = cv.VideoCapture('video1.avi')

cv.destroyAllWindows()
video.release()
