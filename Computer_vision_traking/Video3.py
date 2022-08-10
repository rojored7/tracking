#importar librerias
import cv2
import numpy as np

#definir
def ask_for_tracker():
    print('hola, que api quieres usar')
    print ('apriete 0 para BOOSTING: ')
    print ('apriete 1 para MIL: ')
    print ('apriete 2 para KCF: ')
    print ('apriete 3 para TLD: ')
    print ('apriete 4 para MEDIANFLOW: ')
    print ('apriete 5 para GOTURN: ')
    print ('apriete 6 para MOSSE: ')
    print ('apriete 7 para CSRT: ')

    choice = input ('diga cual tracker')

    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()
    if choice == '5':
        tracker = cv2.TrackerGOTURN_create()
    if choice == '6':
        tracker = cv2.TrackerMOSSE_create()
    if choice == '7':
        tracker = cv2.TrackerCSRT_create()

    return tracker

#tracker
tracker = ask_for_tracker()

#nombre del tracker
tracker_name = str(tracker).split()[0][1:]

#capturar el video

cap = cv2.VideoCapture('carros.mp4')

#leer el primer frame

ret,frame = cap.read()

#seleccionar el ROI

roi = cv2.selectROI('frame', frame)

#inicializar el tracker

ret = tracker.init(frame, roi)

#donde pasa la magia
while True:

    #leer la captura
    ret, frame = cap.read()

    #actualizar el tracker
    success, roi = tracker.update(frame)

    #roi para el tuple
    (x,y,w,h) = tuple(map(int, roi))

    #dibujar la recta de moviimineto
    if success:

        ##carga del tracking
        pts1 = (x,y)
        pts2 = (x+w, y+h)
        cv2.rectangle(frame,
                      pts1,
                      pts2,
                      (255,125,25),
                      3)
    #else
    else:

        print('la cago')
        #failure on traking
        #cv2.PutText(frame,
         #           'LA CAGO MK',
          #          (100,200),
           #         cv2.FONT_HERSHEY_SIMPLEX,
            #        1,
             #       (25,125,255),
              #      3)

    #display tracker
    print('sigaaa')          
    #cv2.putTetx(frame,
     #           tracker_name,
      #          (20,400),
       #         cv2.FONT_HERSHEY_SIMPLEX,
        #        1,
         #       (255,255,0),
          #      3)

    #display resultados
    cv2.imshow(tracker_name, frame)

    #romprer el bucle
    if cv2.waitKey(15) & 0xFF == 27:
        break

#cerrar todo
cap.release()
cv2.destroyAllWindows()    

