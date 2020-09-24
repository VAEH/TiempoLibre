#Ejercicio en el que consta calcular los valores a y b de una funcion lineal
# determinar la ley subyacente a la cual un fenomeno obedece
#En este caso, dependencia lineal de dos observaciones
#Valores dados: x1,y1,x2,y2
#Se utilizo dos métodos y la función format()

try:
    with open('RetosCodeAbbey/linearFunction.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []

def pendiente(x1,y1,x2,y2):
    m = ( (y2-y1) / (x2-x1))
    return m

def valorB (y1,x1, pendi ):
    b = (y1 - (pendi*x1))
    return b 

for linea in lineas:
    x1,y1,x2,y2 = [int(x) for x in linea]
    #print('x',x1,'y', y1)
    m = pendiente(x1,y1,x2,y2) #Calcula la pendiente (a)
    b = valorB(y1, x1, m)#Calcula el valor de B, utilizando la pendiente
    #resultado = (m, b)
    answer.append( '({0} {1})'.format(int(m), int(b))) #Utiliza .format() para imprimir el valor
    prueba = " ".join(map(str,answer))
print(prueba)

#Forma en como se publico en CodeAbbey
'''
scores = int(input())
answer=[]

def pendiente(x1,y1,x2,y2):
    m = ( (y2-y1) / (x2-x1))
    return m

def valorB (y1,x1, pendi ):
    b = (y1 - (pendi*x1))
    return b

for linea in range(scores):
    x1,y1,x2,y2 = [int(x) for x in input().split()]
    #print('x',x1,'y', y1)
    m = pendiente(x1,y1,x2,y2)
    b = valorB(y1, x1, m)
    #resultado = (m, b)
    answer.append( '({0} {1})'.format(int(m), int(b)))
    prueba = " ".join(map(str,answer))
print(prueba)
'''