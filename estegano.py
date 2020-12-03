"""
Antes de nada, debemos instalar el OpenCV y Numpy. Para ello, simplemente tebemos de poner en el terminal (opción que podemos
encontrar en la barra de abajo) estos dos comandos:
pip install opencv-python
pip install numpy==1.19.3
"""

import cv2  # Importamos el paquete cv2, que hemos instalado previamente
import time  # Importamos el paquete time, usado para dar realismo y embellecer la ejecución


class Color:  # Añadimos clases para darle estilos a las cadenas.
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def generacod(mensaje):  # Con esta función transformamos la cadena de texto que queremos
    for c in mensaje:  # ocultar a cada letra en unicode, para obtener la cadena de números que se ocultará.
        yield ord(c)  # Los resultados se van ofreciendo uno a uno con yield, para que luego next los recoja


def get_imagen(imagen):  # Con esta función extraemos la imagen de la dirección suministrada.
    imagen = cv2.imread(imagen, cv2.IMREAD_UNCHANGED)
    return imagen


def codifica(imagen, mensaje):  # Esta es la función más importante, la que inserta el mensaje secreto en la imagen
    imagen = get_imagen('proyimag1T.png')  # Comenzamos recogiendo la imagen con la función anterior
    mensajegenerado = generacod(mensaje)  # Aquí obtenemos el mensaje codificado que le hemos proporcionado
    for i in range(len(imagen)):  # Con estos bucles vamos a ir pixel por pixel añadiendo el unicode de cada letra
        for j in range(len(imagen[0])):
            try:  # con try vamos relizando la acción hasta que next no le ofrezca más resultados
                imagen[i][j][0] = next(mensajegenerado)
            except StopIteration:  # Cuando la función mensajegenerado no da más resultados salta el error StopIteration
                imagen[i][j][0] = 0  # Y al saltar, añadimos un 0, que será nuestro código de control. Usamos 0 porque
        return imagen  # es el único caracter que no tiene traducción a unicode, por lo que no hay error


def decodifica(imagen):  # Con esta función decodificamos el mensaje de la siguiente manera:
    imagen = get_imagen('proyimod1T.png')  # leemos la imagen a decodificar
    mensaje = ''  # inicializamos la variable que almacenará la cadena

    for i in range(len(imagen)):  # Y nuevamente vamos pixel a pixel recogiendo el mensaje secreto siempre y cuando sea
        for j in range(len(imagen[0])):  # diferente a 0, nuestro carácter de control.
            if imagen[i][j][0] != 0:
                mensaje = mensaje + chr(imagen[i][j][0])
            else:
                return mensaje


def escalagris(imagen):  # Esta función se encarga de, con la funcionalidad de cv2 cvtColor, cambiar el color de
    imagen = get_imagen('proyimod1T.png')  # toda la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return gris


def menu():  # Creamos el menu
    print()
    print((Color.BOLD + "APLICACIÓN ESTEGANO" + Color.END).center(100, ' '))
    print()
    print("1) Instertar mensaje oculto en una imagen".center(90, ' '))
    print("2) Extraer mensaje oculto de una imagen".center(88, ' '))
    print("3) Convertir la imagen a escala de grises".center(90, ' '))
    print("4) Salir\n".center(58, ' '))


while True:
    menu()
    OpcionMenu = input(Color.BOLD + "                        Opción: " + Color.END)
    if OpcionMenu == '1':
        print(Color.BOLD + 'OPCIÓN: Insertar mensaje oculto en una imagen' + Color.END)
        alto = get_imagen('proyimag1T.png').shape[0]  # con .shape calculamos el alto y el ancho de la imagen
        ancho = get_imagen('proyimag1T.png').shape[1]
        print()
        print(f'proyimag1T.png tiene {ancho} de ancho y {alto} de alto.')
        cv2.imshow('Imagen original', get_imagen(
            'proyimag1T.png'))  # mostramos la imagen con imshow, siendo el primer parámetro el nombre de la ventana
        cv2.waitKey(0)  # con waitkey hacemos que hasta que la imagen que mostramos no se cierre, no siga el programa
        time.sleep(2)  # con el paquete time generamos un pequeño delay para darle más dinamismo al código
        print()
        mensaje = input(str('Introduzca el mensaje de texto a ocultar: '))
        time.sleep(1)
        print()
        print('Insertando el texto en la imagen...')
        proyimod1T = codifica('proyimag1T.png', mensaje)  # aquí llamamos a la función codificadora, que almacena
        # la imagen ya modificada en una variable.
        cv2.imwrite("proyimod1T.png", proyimod1T)  # Con imwrite guardamos la imagen en un archivo nuevo recien generado

        original = cv2.imread('proyimag1T.png')  # a partir de aquí nos dedicamos a comparar las imágenes
        estegano = cv2.imread('proyimod1T.png')
        time.sleep(1)
        if original.shape == estegano.shape:  # primero por su tamaño
            diferencia = cv2.subtract(original, estegano)  # Y luego por la sustracción de color. Si al sustraer el
            b, g, r = cv2.split(diferencia)  # color de un pixel respecto al de la otra imagen, da 0, es decir sin color
            # Significa que las imágenes son literalmente iguales, pixel a pixel, si al hacer la resta no da 0,
            # significa que el pixel es diferente.
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                print()
                print('Son completamente iguales')
            else:
                print()
                print('El fichero proyimag1T.png es diferente a proyimod1T.png')
        else:
            print()
            print('Las imágenes no son ni del mismo tamaño')

        cv2.imshow('Con texto oculto', estegano)
        cv2.waitKey(0)

    if OpcionMenu == '2':
        print(Color.BOLD + 'OPCIÓN: Extraer mensaje oculto en una imagen' + Color.END)
        time.sleep(1)
        print()
        print('El fichero de la imagen con texto oculto se llama: proyimod1T.png')
        time.sleep(1)
        print()
        print('Extrayendo el texto de la imagen...')
        time.sleep(1)
        print()
        print('El texto oculto es:', (decodifica('proyimod1T.png')))  # aquí llamamos la función decodificadora
        time.sleep(2)

    if OpcionMenu == '3':
        print(Color.BOLD + 'OPCIÓN: Convertir la imagen a escala de grises' + Color.END)
        print()
        time.sleep(1)
        print('El fichero de la imagen con texto oculto se llama: proyimod1T.png')
        print()
        time.sleep(1)
        print('Convirtiendo la imagen a escala de grises...')

        proyimgr1T = escalagris('proyimag1T.png')  # Y aquí llamamos a la función que cambia la imagen a escala
        # de grises, para luego guardarla con iwrite y mostrarla con show

        cv2.imwrite("proyimgr1T.png", proyimgr1T)

        cv2.imshow('Escala de grises', proyimgr1T)

        cv2.waitKey(0)
        time.sleep(2)

    if OpcionMenu == '4':  # Con esta última opción cerramos el programa
        print('Cerrando sesión en el programa...')
        time.sleep(2)
        break

    else:  # Y por último, controlamos que el usuario no pueda introducir otro valor.
        print()
        print('El valor seleccionado no es valido, introduzca un valor válido'.center(110, ' '))
