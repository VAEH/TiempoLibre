
#Coge el input (Entrada y saca el valor minimo )
#Obviamente hay forma más sencilla que es utilizar (max - min) que son propias de python 
"""
numeros = input()
maximo=0
minimo=0
c = []
#forma sencilla de convertir una entrada en una lista
convertList = [int(x) for x in numeros.split()]

for dato in convertList:
    if dato>maximo:
        maximo=dato
    elif dato<minimo:
        minimo= dato
c.append(maximo)
c.append(minimo)
prueba = " ".join(map(str, c))
print(prueba)
"""

#Ejercicio original Utilizando un archivo txt

try:
    scores = open("DatamaximunArray.txt", "r")
    print('exito!')
except:
    print("Prueba fallida")
maximo=0
minimo=0
c = []
for linea in scores:
    convertLista= [int(x) for x in linea.split()]

for dato in convertLista:
    if dato>maximo:
        maximo=dato
        #c.append(maximo)
    elif dato<minimo:
        minimo= dato
        #c.append(minimo)
c.append(maximo)
c.append(minimo)
prueba = " ".join(map(str, c))
print(prueba)


#Otra versión para la misma solución 
"""
def findRange(numbers):
    answer = []
    minNum, maxNum = 0,0
    numbers = numbers.split()
    for x in numbers:
        if int(x) < int(minNum):
            minNum = x
        if int(x) > int(maxNum):
            maxNum = x
    print(str(maxNum) + " " + str(minNum))
findRange(raw_input())

"""