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
    with open('RetosCodeAbbey/MaximoComunDivisor.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:] #Obvia la primer linea
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []
for linea in lineas:
    mcd =0
    res =0
    num1,num2 = [int (x) for x in linea]
    a = max(num1, num2)
    b =min(num1, num2)
    while b!=0:
        res = b
        b = a%b
        a =res
    #Formula para calcular el MCM
    mcm = (num1*num2)/(res)
    #aux = (mcd, mcm)
    #answer.append((res, int(mcm)))
    answer.append('('+str(res)+' '+str(int(mcm))+')')
    #x = " ".join(map(str, answer))
    #print(x)
poto = " ".join(answer)
print(poto)

#Forma en como se publico en CodeAbbey 
'''
scores = int(input())
answer = []

for linea in range(scores):
    mcd =0
    res =0
    num1,num2 = [int (x) for x in input().split()]
    a = max(num1, num2)
    b =min(num1, num2)
    while b!=0:
        res = b
        b = a%b
        a =res
    #Formula para calcular el MCM
    mcm = (num1*num2)/(res)
    #aux = (mcd, mcm)
    answer.append('('+str(res)+' '+str(int(mcm))+')') #Append() solo recibe un argumento, por eso la forma de guardar el dato, ya que agregamos son dos    #print(answer)
poto = " ".join(answer)
print(poto)
'''

