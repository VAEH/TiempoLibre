import math 
try:
    scores = open("RetosCodeAbbey/vowelCount.txt", "r")
    print('exito!')
except:
    print("Prueba fallida")
c=[]
contador=0
abece=["a", "e","i","o","u","y"]

for linea in scores:
    lineaList=linea.split()
    #print(lineaList)
    for campo in lineaList:
        #print(campo)
        for i in campo:
            #print('imprime campo:',i)
            for letra in abece:
                #print('imprime letra', letra)
                if i==letra:
                    contador+=1
    c.append(contador)
    contador=0
c = " ".join(map(str, c))
print(c)
    
#print(c)

#Forma en como se publico en CodeAbbey, Utilizando input()
'''
scores = int(input())
c=[]
contador=0
abece=["a", "e","i","o","u","y"]
for linea in range(scores):
    #print('esto: ', scores)
    lineaList = input().split()
    #print(prueba)
    for campo in lineaList:
        #print(campo)
        for i in campo:
            #print('imprime campo:',i)
            for letra in abece:
                #print('imprime letra', letra)
                if i==letra:
                    contador+=1
    c.append(contador)
    contador=0
c = " ".join(map(str, c))
print(c)

'''
#Una forma de hacerlo en Codeabbey Cogiendo los datos de entrada(Por probar)
'''
total = input()
listatotal = [1 * x for x in range(int(total))]
resultado = []
for num in listatotal:
    z = input()
    sum = z.count("a") + z.count("e") + z.count("i") + z.count("o") + z.count("u") + z.count("y")      
    resultado.append(sum)
print (*resultado)
'''

#Este ejercicio me escupio en la cara literal
'''
n = int(input())
for j in range(n):
    v = 0
    for x in input():
        if x in 'iaeyuo':
            v += 1
    print( v )
'''