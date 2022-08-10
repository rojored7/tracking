#importar librerias
import cv2

#Tomar el video
cap= cv2.VideoCapture(0)

#por si el path esta mal
if cap.isOpened() == False:
    print('error¡ revisate el path')

#la magia sucede aqui
while cap.isOpened():

    ret, frame = cap.read()

    if ret == True:

        cv2.imshow('frame',frame)

        if cv2.waitKey(15) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows
    
