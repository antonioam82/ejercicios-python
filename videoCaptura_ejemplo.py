import cv2

captura = cv2.VideoCapture(0)
#captura = cv2.VideoCapture('videoSalida.avi')
#salida=cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
while(captura.isOpened()):
    ret,imagen=captura.read()
    if ret==True:
        cv2.imshow('video',imagen)
        #salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):#(40)
            break
    #else:
        #break
captura.release()
#salida.release()
cv2.destroyAllWindows()
