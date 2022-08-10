#importar librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt 


#deteccion de caras
face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#definir funcion
def detect_face(img):
    face_img = img.copy()
    face_rectangle = face_cascade.detecMultiScale(face_img)

    for (x,y,w,h) in face_rectangle:
        cv2.rectangle(face_img,(y,x),(x+w, y+h), (255,255,255),10)
    return face_img


#tomar video
cap = cv2.VideoCapture(0)

#aqui pasa la magia
while True:

    #captura de video
    ret, frame = cap.read()

    #mostrar
    cv2.imshow('frame', frame)

    #romprer el bucle
    if cv2.waitKey(15) & 0xFF == 27:
        break

#cerrar todo
cap.release()
cv2.destroyAllWindows()    
