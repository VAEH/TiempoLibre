"""
Ejemplo: N°1
    Para cada linea del fichero representado por el manejador, añade
    una unidad a la variable contador.
""" 
"""
manf = open('mbox.txt')
contador =0
for linea in manf:
    contador =contador+1
print('lineas contabilizadas', contador)

"""


"""
Ejemplo N°2
    Si sabes que el fichero es relativamente peque˜no comparado con el tama˜no de
    tu memoria principal, puedes leer el fichero completo en una cadena usando el
    m´etodo read sobre el manejador del fichero.
"""
"""
manf = open('mbox-short.txt')
ent = manf.read()
print (len(ent))
#Imprime los priemeros 20 caracteres utilizando slicing
print(ent[:20])
"""

"""
Ejemplo N°3
    Por ejemplo, si queremos leer un fichero y mostrar unicamente las l´ıneas que comienzan
    con el prefijo “From:”, podemos usar el m´etodo de cadena startwith para
    seleccionar solamente aquellas l´ıneas con el prefijo deseado:
"""
"""
manf = open('mbox-short.txt')
for linea in manf:
    if linea.startswith('From:'):
        print (linea)
"""
"""
EjemploN°3 - version mejorada
    Podr´ıamos usar rebanado de l´ıneas para imprimir todo menos el ´ultimo car´acter,
    pero un enfoque m´as sencillo consiste en usar el m´etodo rstrip, que retira los espacios
    en blanco de la parte derecha de una cadena, como se muestra a continuaci ´on:
"""
"""
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    if linea.startswith('From:') :
        print (linea)
"""

"""
Ejemplo N°4 - Utilizando Continue
    Se re estructura el diseño para saltar e ignorar aquellas lineas que no nos interesan.

"""
"""
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
# Saltar 'l´ıneas que no nos interesan'
    if not linea.startswith('From:') :
        continue
# Procesar nuestra l´ınea 'interesante'
    print (linea)
"""
"""
Ejemplo N°5 - Se utiliza el método find para encontarar solo los correos de la Universidad de Sudafrica y devuelve -1 si
    Sino se encuentran.
manf = open('mbox-short.txt')
for linea in manf:
    linea = linea.rstrip()
    if linea.find('@uct.ac.za') == -1 :
        continue
    print (linea)
"""

"""
Ejemplo N°6 - Permitir al usuario agregar el nombre del fichero a consultar
    Se pide al usuario que agregue el nombre de un fichero al cual quiera consultar y se recibe mediante el método
    raw_input() que recibe la información siempre como una cadena de caracteres directamente del teclado.
"""
"""
nombref = raw_input('Introduzca el nombre del fichero: ')
manf = open(nombref)
contador = 0
for linea in manf:
    if linea.startswith('Subject:') :
        contador = contador + 1
print ('Hay', contador, 'l´ıneas subject en', nombref)
"""

"""
Ejemplo 7 - Version mejorada del ejemplo 6 con try - catch
"""
"""
nombref = input('Introduzca el nombre del fichero: ')
try:
    manf = open(nombref)
except:
    print ('No se pudo abrir el fichero:', nombref)
    exit()
contador = 0
for linea in manf:
    if linea.startswith('Subject:') :
        contador = contador + 1
print ('Hay', contador, 'l´ıneas subject en', nombref)
"""

"""
Ejercicios N°8 - Control de deupracion utilizando la funcion de Python "repr"
s = '1 2\t 3\n 4'
print (repr(s))

"""
"""
EEjercicio N° 9 - ejercicios propuestos en el libro
    Escribe un programa que lea un fichero e imprima en pantalla su
    contenido (l´ınea a l´ınea), todo en may´usculas. La ejecuci ´on del programa deber´ıa
    ser algo similar a esto:
"""
"""
fichero = input('Ingresa Un fichero')
fichero = open(fichero)
for linea in fichero:
    linea= linea.rstrip().upper()
    print(linea)
"""

fichero = input('Ingresa Un fichero')

fichero = open(fichero)
cont=0

for linea in fichero:
    if not linea.startswith(''):
        print('No se que debeia imprimir aca')