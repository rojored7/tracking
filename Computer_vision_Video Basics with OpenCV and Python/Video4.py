#importar librerias
import cv2

#definir librerias
def draw_rectangle(event, x, y, flags, param):

    #declarar variables globales
    global pt1, pt2, tope_left_clicked, bottom_right_clicked

    #crear evento de boton
    if event == cv2.EVENT_LBUTTONDOWN:

        #resetear el rectangulo
        if top_left_clicked == True and bottom_right_clicked == True:

            #puntos iniciales
            pt1 = (0,0)
            pt2 = (0,0)

        #valor inicial de falso

        top_left_click = False
        bottom_right_clicked = False

    #revisar el estado del boton

    if top_left_clicked == False:
        pt1 = (x,y)
        top_right_clicked = True

    elif bottom_right_clicked == False:
        
        pt2 = (x,y)
        bottom_right_clicked = True

#puntos iniciales
pt1 = (0,0)
pt2 = (0,0)

#marcadeores falsos

top_left_clicked = False
bottom_right_clicked = False

#Tomar el video
cap= cv2.VideoCapture(0)

#crear nueva ventana

cv2.namedWindow('test')

#calback de mouse

cv2.setMouseCallback('test', draw_rectangle)

#aqui pasa la magia

while True:

    #captura de frame
    ret, frame = cap.read()

    #base de las variables
    if top_left_clicked == True:
        cv2.circle(frame,center=pt1, radius=5, color=(255,0,0),thickness=-1)
    #dibujar un rectangulo en el centro
    if top_left_clicked == True and bottom_right_clicked == True:
        cv2.rectangle(frame,pt1,pt2,(0,255,0),3)

    #mostrar
    cv2.imshow('frame', frame)

    #romprer el bucle
    if cv2.waitKey(15) & 0xFF == 27:
        break

#cerrar todo
cap.release()
cv2.destroyAllWindows()    




