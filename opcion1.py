import cv2


def generacod(mensaje):
    for c in mensaje:
        yield ord(c)


def get_imagen(imagen):
    imagen = cv2.imread(imagen, cv2.IMREAD_UNCHANGED)
    return imagen


def codifica(imagen, mensaje):
    imagen = get_imagen('proyimag1T.png')
    mensajegenerado = generacod(mensaje)
    for i in range(len(imagen)):
        for j in range(len(imagen[0])):
            try:
                imagen[i][j][0] = next(mensajegenerado)
            except StopIteration:
                imagen[i][j][0] = 0
        return imagen


def decodifica(imagen):
  imagen = get_imagen('proyimod1T.png')
  mensaje = ''

  for i in range(len(imagen)):
    for j in range(len(imagen[0])):
        if imagen[i][j][0] != 0:
          mensaje = mensaje + chr(imagen[i][j][0])
        else:
            return mensaje

def escalagris(imagen):
    imagen = get_imagen('proyimod1T.png')
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return gris


alto = get_imagen('proyimag1T.png').shape[0]
ancho = get_imagen('proyimag1T.png').shape[1]
canal = get_imagen('proyimag1T.png').shape[2]

print('proyimag1T.png tiene', ancho, 'de ancho y', alto, 'de alto.')

cv2.imshow('Imagen original', get_imagen('proyimag1T.png'))

cv2.waitKey(0)

mensaje = input(str('Introduzca el mensaje de texto a ocultar: '))

print('Insertando el texto en la imagen...')

proyimod1T = codifica('proyimag1T.png', mensaje)
cv2.imwrite("proyimod1T.png", proyimod1T)


original = cv2.imread('proyimag1T.png')
estegano = cv2.imread('proyimod1T.png')

if original.shape == estegano.shape:
    difference = cv2.subtract(original, estegano)
    b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print('Son completamente iguales')
    else:
        print('El fichero proyimag1T.png es diferente a proyimod1T.png')
else:
    print('Las imágenes no son ni del mismo tamaño')

cv2.imshow('Con texto oculto', estegano)

cv2.waitKey(0)


print('El fichero de la imagen con texto oculto se llama: proyimod1T.png')

print('Extrayendo el texto de la imagen...')

print('El texto oculto es:', (decodifica('proyimod1T.png')))


print('El fichero de la imagen con texto oculto se llama: proyimod1T.png')
print('Convirtiendo la imagen a escala de grises...')

proyimgr1T = escalagris('proyimag1T.png')

cv2.imwrite("proyimgr1T.png", proyimgr1T)

cv2.imshow('Escala de grises', proyimgr1T)

cv2.waitKey(0)
