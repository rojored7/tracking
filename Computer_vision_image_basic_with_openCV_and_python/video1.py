#importar librerias 
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

#Cargar la imagen
img = Image.open('spacex.jpg')
#Rotar la imagen
"img=img.rotate(-90)"
#Revisar el tipo de imagen
print(type(img))
#convertir una imagena a un arregrlo
img_array = np.asarray(img)
#tamaño del arreglo
n=img_array.shape
print(n)
#plotear la imagen
plt.imshow(img_array)
plt.show()
#imagen para proceso
img_test = img_array.copy()
#lectura canal red
#chanel red = 0
#chanel green = 1
#chanel blue = 2
plt.imshow(img_test[:,:,0])
plt.show()
#mapeo en escala de grises del canal red
plt.imshow(img_test[:,:,0],cmap='gray')
plt.show()
#remover el color del canal
img_test[:,:,1]=0
plt.imshow(img_test)
plt.show()
