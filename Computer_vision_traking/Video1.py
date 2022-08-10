#importar librerias
import cv2
import numpy as np

#parametros para shi-tomasi deteccion de esquinas

st_params = dict(maxCorners=30,
                qualityLevel=0.2,
                minDistance=2,
                blockSize=7)

#parametros de Lucas-Kande para flujo optico
lk_params = dict(winSize=(15,15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1))

#captura de video
cap = cv2.VideoCapture('run.mp4')

#color frames
color = (0,255,0)

#leer el primer frame 
ret, first_frame = cap.read()

#convertir a gray

prev_gray = cv2.cvtColor(first_frame,
                         cv2.COLOR_RGB2GRAY)

#encontrar las esquinas mas fuertes en el fotograma

prev = cv2.goodFeaturesToTrack(prev_gray,
                               mask=None,
                               **st_params)

#crear una imagen del mismo tamaño que el frame para dibujar

mask = np.zeros_like(first_frame)

#donde pasa la magia

while(cap.isOpened()):

    #leer el frame
    ret, frame = cap.read()

    #convertir 
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    #calcular el flujo optico por Lucas-Kanade
    next, status, error = cv2.calcOpticalFlowPyrLK(prev_gray, gray,  prev, None, **lk_params)

    #Seleccion de posicion previua

    good_old=prev[status==1]

    #seleccioon siguiente posicion

    good_new=next[status==1]

    #dibujar el flujo optico

    for i , (new,old) in enumerate(zip(good_new,good_old)):

        #retornar coordenadas del nuevo punto
        a,b = new.ravel()

        #retornar coordenadas del viejo punto

        c,d = old.ravel()

        #dibujar una linea

        mask = cv2.line(mask,
                        (a,b),
                        (c,d),
                        color,
                        2)

        #dibujar un circulo relleno

        frame = cv2.circle(frame,
                           (a,b),
                           3,
                           color,
                           -1)

        #mostrar el flujo en el frame original

        output = cv2.add(frame,mask)

        #actualizar el siguiente frame

        prev_gray = gray.copy()

        #actualizar el siguiente

        prev = good_new.reshape(-1,1,2)

        #abrir nueva ventana

        cv2.imshow("optical flow", output)

        #romprer el bucle
        if cv2.waitKey(15) & 0xFF == 27:
            break

#cerrar todo
cap.release()
cv2.destroyAllWindows()           
    
