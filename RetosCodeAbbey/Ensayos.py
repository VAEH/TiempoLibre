""""

lines = """#13 14
    #234 2345
    #3456 7854"""
"""
for line in lines.splitlines():
    print(lines)
    #num1, num2 = map(int, line.split())
    #print(num2-num1)
"""
'''
#Esto es una forma de abrir y convertir un txt en una lista
with open('RetosCodeAbbey/SumOfDigits.txt', 'r') as f:
    lineas = [linea.split() for linea in f]
print(lineas)

for linea in lineas:
    print(linea)
'''

import math 

try:
    with open('RetosCodeAbbey/SortBubble.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:] #Obvia la primer linea
        print('Exito!')
        
except:
    print("Prueba fallida")

for linea in lineas:
    lista = [int(x) for x in linea]
    #tamaño = len(lista)
j = 1
contador = 1
prueba = 1
for i in range(len(lista)-1):
    prueba+=1
    #print(i)
    if lista[i] > lista[j] :
        t = lista[i]
        lista[i] = lista[j]
        lista[j] = t
        j+=1
        contador+=1
    else:
        j+=1
print(str(contador), str(round( (prueba**2)/4) ))

