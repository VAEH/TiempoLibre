#Se te dará el vector para el cual la suma de verificación debería ser 
# calculada. Realiza los cálculos como sigue: adiciona cada elemento del 
# vector (iniciando desde el comienzo) a la variable resultado y multiplica 
# esta suma por 113 - el módulo o residuo de este nuevo valor entre 10000007 
# se convertiría en el nuevo valor de la variable resultado, y así sucesivamente.

#ejemplo del ejercicio: https://www.codeabbey.com/index/wiki/checksum
#Tuve en cuenta la lognitud tanto del resultad como del límite
#Aunque habia una forma más sencilla -_-
#No pude hacerlo en una función, al momento de imprimir sucedia algo con un contador
#La idea estuvo bien desde el inicio, solo que fallo al implmentarlo en un método o función
try:
    with open('RetosCodeAbbey/checkSum.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []


    
   
#CheckSum(1234)
#resultado =0
for linea in lineas:
    #n = len(linea)
    #print(n)
    resultado =0
   # print('resultadooo', resultado)
    for  numero in linea:
        limite = 10000007
        taLimite = len(list(str(limite)))
        resultado = (resultado + int(numero))*113
        tamaño=len(list(str(resultado)))
        if tamaño> taLimite:
            resultado =  (resultado % limite)
    print(str(resultado))

#Forma en que se publico en CodeAbbey
'''
# coding: utf-8
# Your code here!
scores = int(input())

lineas = input().split()
resultado =0
for numero in lineas:
    limite = 10000007
    taLimite = len(list(str(limite)))
    resultado = (resultado + int(numero))*113
    tamaño=len(list(str(resultado)))
    if tamaño> taLimite:
        resultado =  (resultado % limite)
print(str(resultado))

'''

#Una forma que me niego en creer que haya funcionado -_-
'''
lenght = int(input())
nums=[int(i) for i in input().split()]
result=0
for i in nums:
    result = (result+i)*113
    result = result%10000007
print(result)
'''

#Otra forma
'''
n=int(input())
l=[]
result=0
string=input().split()
for i in range(n):
    l.append(int(string[i]))
    #print(l[i])
    result=(result+l[i])*113
    if result>10000007:
        result=result%10000007
print(result)
'''