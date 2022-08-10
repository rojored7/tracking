#importar librerias
import cv2

#Tomar el video
cap= cv2.VideoCapture(0)

#definir alto y ancho del video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

#esquina derecha superior

x = width // 2
y = height // 2

#rectangulo tamaño

w = width // 4
h = height // 4

#la magia

while True:

    ret, frame = cap.read()

    #frame reactangular
    cv2.rectangle(frame,(x,y),(x+w, y+h), color = (255,0,255),thickness=5)

    cv2.imshow('frame',frame)

    if cv2.waitKey(15) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows    
