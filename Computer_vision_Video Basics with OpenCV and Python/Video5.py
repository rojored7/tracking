#importar librerias
import cv2

#definir librerias
def draw_circle(event, x, y, flags, param):


    global center, clicked
    #traker
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        clicked = False
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

#centro del circulo
centro = (0,0)
clicked = False

#tomar video
cap = cv2.VideoCapture(0)

#crear ventana
cv2.namedWindow('prueba')

#calback
cv2.setMouseCallback('prueba',draw_circle)

#aqui pasa la magia
while True:

    #captura de video
    ret, frame = cap.read()

    #si el click
    if clicked:
        cv2.circle(frame,center=center,radius=50,color=(255,0,0),thickness=3)

    #mostrar
    cv2.imshow('frame', frame)

    #romprer el bucle
    if cv2.waitKey(15) & 0xFF == 27:
        break

#cerrar todo
cap.release()
cv2.destroyAllWindows()    
 
