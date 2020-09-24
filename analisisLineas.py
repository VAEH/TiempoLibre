"""
querran encontrar las “l´ıneas interesantes” y luego parsear (analizar) cada una de
ellas para buscar alguna parte importante en su interior. ¿Qu´e ocurre si queremos
imprimir el d´ıa de la semana de aquellas l´ıneas que comienzan por “From ”?

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

El m´etodo split es muy efectivo cuando nos enfrentamos con este tipo de problemas.
Podemos escribir un peque˜no programa que busque las l´ıneas que comiencen
por “From ”, extraer las palabras de esas l´ıneas con split, y luego imprimir en
pantalla la tercera palabra de cada una:

"""

manf = open('mbox-short.txt')
for linea in manf:
    #linea = linea.rstrip()
    if not linea.startswith('From ') : continue
    palabras = linea.split()
    print(palabras[2])