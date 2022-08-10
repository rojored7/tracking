#importar librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

#definir variables
drawing = False
ex = -1
ey = -1

#definir funciones
#boton derecho

def draw_rectangle(event, x, y, flags, param):

    global ex, ey, drawing

    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ex,ey = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ex,ey),(x,y,),(35,69,78),-1)
            
    elif event == cv2.EVENT_LBUTTONUP:

        drawing = False
        
        cv2.rectangle(img,(ex,ey),(x,y,),(35,69,78),-1)

#conectar con el callback

cv2.namedWindow(winname='intento_1')

#callback

cv2.setMouseCallback('intento_1',draw_rectangle)

#crear una imagen en negro para trabajar
img = np.zeros(shape=(512,512,3),dtype=np.int8)

#ejecucion

while True:

    cv2.imshow('intento_1',img)

    #tecla esc para salir o para una tecla se puede poner ord('TECLA')

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows
