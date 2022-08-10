#importar librerias
import cv2

#Tomar el video
cap= cv2.VideoCapture(0)

#definir alto y ancho del video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

#salida de video

output = cv2.VideoWriter('video.mkv',cv2.VideoWriter_fourcc(*'DIVX'),\
                          20,(width,height))

#donde ocurre la magia

while True:

    ret,frame = cap.read()

    #operaciones
    output.write(frame)

    #si se quiere en BN
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', gray)
    cv2.imshow('frame', frame)

    #cerrar ventana con mantener oprimido esc

    if cv2.waitKey(5) & 0xFF == 27:
        break

#destruir todas las ventanas al terminar siempre
cap.release()
output.release()
cv2.destroyAllWindows
