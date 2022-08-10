#importar librerias
import cv2
import numpy as np


#captura de video
cap = cv2.VideoCapture('chaplin.mp4')


#leer el primer frame 
ret, first_frame = cap.read()

#convertir a gray

prev_gray = cv2.cvtColor(first_frame,
                         cv2.COLOR_RGB2GRAY)

#crear una imagen delde mimso tamaño

mask = np.zeros(first_frame, dtype=np.uint8)

#saturacion maxima

mask[...,1]  = 255

#donde pasa la magia
while(cap.isOpened()):

    #leer el frame
    ret, frame = cap.read()

    #convertir 
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    #calculo del flujo denso por farnesback
    flow = cv2.calcOpticalFlowFarneback(prev_gray,
                                        gray,
                                        None,
                                        0.5,
                                        3,
                                        15,
                                        3,
                                        5,
                                        1.2,
                                        0)
    #maginitud del angulo
    magn, angle = cv2.cartToPolar(flow[..., 0],
                                  flow[..., 1])

    #set a la imagen dependiendo de la direccion del flujo optico
    mask[..., 0] = angle*180/np.pi/2

    #normalizar la magnitud
    mask[..., 2] = cv2.normalize(magn,
                                 None,
                                 0,
                                 255,
                                 cv2.NORM_MINMAX)

    #convertir de HSV a RGB
    rgb = cv2.cvtColor(mask, cv2.COLOR_H2V2RGB)

    #abir nueva ventana

    cv2.imshow("flujo denso", rgb)

    #romprer el bucle
    if cv2.waitKey(15) & 0xFF == 27:
        break

#cerrar todo
cap.release()
cv2.destroyAllWindows()         

    
    
