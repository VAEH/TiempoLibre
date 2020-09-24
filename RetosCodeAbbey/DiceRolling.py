 #convertir valores aleatorios en puntos de dados 
 # específicos. El objetivo de esta tarea es dar una 
 # práctica en la simulación de dados rodando por los 
 # valores procedentes de un generador de números aleatorios.

#Formula según el autor
#floor(x*(b-a)+a)
#floor(x) devuelve el entero más grande no mayor que x

#Answer should contain numbers from 1 to 6 for each of input values, 
#produced by the discussed algorithm.
import math 

try:
    with open('RetosCodeAbbey/DiceRolling.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []

n = 6 #Cantidad de caras de un cuadrado
#print(n)
#Método que convierte a tipo Int y separa datos
#Se obtiene el numero de la cara del dado tipo INt
def diceRoller(numero, n):
    decimal, entero = math.modf(float(numero)*n)
    entero = int(entero) +1
    return entero
    #print(entero)

for linea in lineas:
    numero= "".join(linea)
    #print(numero)
    answer.append(diceRoller(numero,n))
print(*answer, sep=" ")

#Forma que descubri como sacar un rango o la cantidad de numeros con input()
'''
scores = int(input())
contador = 0
answer=[]
for linea in range(scores):
    contador +=1
'''
#Forma en como se publico en CodeAbbey
'''
import math

scores= int(input())
contador = 6

#print(contador)
def diceRoller(numero, n):
    decimal, entero = math.modf(float(numero)*n)
    entero = int(entero) +1
    return entero
    #print(entero)

for linea in range(scores):
    numero = [x for x in input()]
    numero= "".join(numero)
    answer.append(diceRoller(numero,contador))
print(*answer, sep=" ")
'''