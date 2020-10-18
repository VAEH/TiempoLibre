"""
APROXIMACIÓN RAIZ CUADRADA

Muchos problemas matemáticos en programación no son resueltos exactamente, sino aproximadamente, 
mediante varias computaciones del resultado, cada de una de las cuales se acerca cada vez más al objetivo


    1. Busca la raíz cuadrada r del valor dado X.
    2. Usa algún valor arbitrario, por ejemplo r = 1 como la primera aproximación (seguramente no es la más adecuada).
    3. Para un cálculo apropiado de la raíz cuadrada, la ecuación r = X / r debe cumplirse.
    4. Calcula d = X / r (d no sería igual a r, ya que r no es la raíz exacta).
    5. Toma el promedio entre r y d como la nueva aproximación.

Formula: r = (r + (X/r))/2

Se nos dan entonces valores de X para los cuales se realizarán los cálculos y el número de iteraciones N a ejecutar.
Usa r = 1 al comienzo, y muestra la aproximación resultante (después de las N iteraciones).

Los resultados deberían tener una precisión de 1e-7 = 0.0000001 o mejor!
"""


try:
    with open('RetosCodeAbbey/SqareRoot.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:] #Obvia la primer linea
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []
#Utiliza 2 argumentos, el valor o dato y la r de raíz que al inicio es 1 y cambia a medida de cada iteracción
def RaizCuadrada(valor, r):
    d = xValor/r
    raiz = (r + d)/2
    r = raiz
    return r

for linea in lineas:
    r=1 #Valor inicial
    prueba =0
    xValor, yItera = [int(x) for x in linea] #Valor e iteracción
    if yItera ==0:     #Se utiliza el condicional porque hay casos en que la iteracción es cero y el resultado entonces es 1 (r=1)
        answer.append('1')
    else:
        for i in range(yItera): #Concional que realiza la iteracción
            prueba = RaizCuadrada(xValor, r) #Utiliza método
            r = prueba
        answer.append(str(prueba))
print(*answer, sep= " ") #Imprime

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

#Otras Formas del ejercicio

'''
#Ejercicio hecho con phyton 2
def root(x, ran2):
    r = 1
    for i in range(ran2):
        r = (r + x / r) / 2.0
    return r
    
ran = int(raw_input())
for i in range(ran):
    x, ran2 = map(int, raw_input().split())
    print root(x, ran2),
'''

#Otra forma
'''
for _ in range(int(input())):
    x, n = map(int, input().split())
    r = 1.00
    if n >= 1:
        for i in range(n):
            d = x / r
            abs(r - d)
            r = (r + d) / 2
        print(r, end=' ')
    else:
        print("1", end=' ')
'''