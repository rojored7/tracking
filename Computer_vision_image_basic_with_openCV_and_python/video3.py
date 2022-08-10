#importar librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

#crear una imagen en negro para trabajar
black_img = np.zeros(shape=(512,512,3),dtype=np.int16)
#Revisar el tipo de imagen
print(type(black_img))
#tamaño de la imagen
n=black_img.shape
print(n)
#dibujar un circulo contorno
cv2.circle(img=black_img,center=(400,100),radius=50,color=(255,0,0),thickness=8)
#dibujar un circulo lleno
cv2.circle(img=black_img,center=(400,200),radius=50,color=(0,255,0),thickness=-1)
#dibujar un rectangulo vacio
cv2.rectangle(black_img,pt1=(200,200),pt2=(300,300),color=(0,255,0),thickness=5)
#dibujar un rectangulo lleno
cv2.rectangle(black_img,pt1=(200,50),pt2=(300,150),color=(60,0,20),thickness=-1)
#dibujar un triangulo vacio
vertices = np.array([[10,450],[11,350],[180,450]],np.int32)
pts = vertices.reshape(-1,1,2)
cv2.polylines(black_img,[pts],isClosed=True,color=(0,0,255),thickness=3)
#dibujar un triangulo lleno
vertices = np.array([[10,250],[110,150],[180,250]],np.int32)
pts = vertices.reshape(-1,1,2)
cv2.fillPoly(black_img,[pts],color=(20,50,40))
#dibujar una linea
cv2.line(black_img,pt1=(512,0),pt2=(0,512),color=(255,255,0),thickness=3)
#escribir
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(black_img,text='rojored96',org=(210,500),fontFace=font,fontScale=3,color=(60,70,20),thickness=3,lineType=cv2.LINE_AA)
#mostrar imagen
plt.imshow(black_img)
plt.show()
