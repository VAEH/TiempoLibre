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
    with open('RetosCodeAbbey/SqareRoot.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:] #Obvia la primer linea
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []
def RaizCuadrada(valor, r):
    d = xValor/r
    raiz = (r + d)/2
    r = raiz
    return r
#print(RaizCuadrada(2))
#print(RaizCuadrada(150))

for linea in lineas:
    r=1
    prueba =0
    xValor, yItera = [int(x) for x in linea]
    if yItera ==0:
        answer.append('1')
    else:
        for i in range(yItera):
            prueba = RaizCuadrada(xValor, r)
            r = prueba
        answer.append(str(prueba))
print(*answer, sep= " ")

'''
#El problema de utilizar el while es cuando hay una resulato o una iteracciòn de cero, donde no se imprime dicho valor (1)
#y en vez de 1 imprime es cero, por eso falla. Además si se utiliza junto con el condicional, no va a evaluar en la iteracción 0 (cero)
    if yItera ==0:
        print(1)
    while yItera!=0:
        yItera-=1
        prueba = RaizCuadrada(xValor, r)
        r = prueba
        #print(d)
    print(prueba)
    #r =0
'''

#Forma en como se publca en CodeAbbey
'''
scores = int(input())
answer = []

def RaizCuadrada(valor, r):
    d = xValor/r
    raiz = (r + d)/2
    r = raiz
    return r

for linea in range(scores):
    r=1
    prueba =0
    xValor, yItera = [int(x) for x in input().split()]
    if yItera ==0:
        answer.append('1')
    else:
        for i in range(yItera):
            prueba = RaizCuadrada(xValor, r)
            r = prueba
        answer.append(str(prueba))
print(*answer, sep= " ")
'''


