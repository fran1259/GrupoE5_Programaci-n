import cv2

imagen = cv2.imread('proyimag1T.png', cv2.IMREAD_UNCHANGED)

dimensions = imagen.shape

alto = imagen.shape[0]
ancho = imagen.shape[1]
canal = imagen.shape[2]

print('proyimag1T.png tiene', ancho, 'de ancho y', alto, 'de alto.')

cv2.imshow('Imagen original', imagen)

cv2.waitKey(0)
