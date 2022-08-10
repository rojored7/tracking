#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import cv2

#Cargar la imagen
img = cv2.imread('spacex.jpg')
#Revisar el tipo de imagen
print(type(img))
#tamaño de la imagen
n=img.shape
print(n)
#mostrar imagen
plt.imshow(img)
plt.show()
#convertir imagen de bgr2rgb
img_fix = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#mostrar imagen
plt.imshow(img_fix)
plt.show()
#leer imagen en escala de grises
img_gray = cv2.imread('spacex.jpg',cv2.IMREAD_GRAYSCALE)
#tamaño de la imagen
n=img_gray.shape
print(n)
#mostrar imagen
plt.imshow(img_gray, cmap='gray')
plt.show()
#redimensionar imagen
img_new = cv2.resize(img_fix,(1000,400))
#mostrar imagen
plt.imshow(img_new)
plt.show()
#redimemncionar con radio
width_ratio = 0.5
height_ratio =0.5
img2 = cv2.resize(img_fix,(0,0),img_fix,width_ratio,height_ratio)
#mostrar imagen
plt.imshow(img2)
plt.show()
#girar en 0 eje horizontal, 1 eje vertical, -1 los dos
img_3 = cv2.flip(img_fix,-1)
#mostrar imagen
plt.imshow(img_3)
plt.show()
#ordenar el canvas
last_img = plt.figure(figsize=(10,7))
ilp = last_img.add_subplot(111)
ilp.imshow(img_fix)
