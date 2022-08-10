#importar librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

#definir funciones
#boton derecho

def draw_circle(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),70,(35,69,78),-1)
#boton izquierdo

    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),30,(105,95,208),-1)        
#conectar con el callback

cv2.namedWindow(winname='intento_1')

#callback

cv2.setMouseCallback('intento_1',draw_circle)

#crear una imagen en negro para trabajar
img = np.zeros(shape=(512,512,3),dtype=np.int8)

#ejecucion

while True:

    cv2.imshow('intento_1',img)

    #tecla esc para salir o para una tecla se puede poner ord('TECLA')

    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows
