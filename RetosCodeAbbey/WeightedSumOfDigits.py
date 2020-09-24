#Ejercicio de Sumas ponderadas utilizando Enumerate()
#Y otro ti´o de métodos como hacerlo en una sola linea -_-

try:
    with open('RetosCodeAbbey/WeightedSumOfDigits.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        #print(lineas)
        
except:
    print("Prueba fallida")
answer = []

#    print(lista)
#Método realiza la suma ponderada de los datos en la lista 
def WeightedSum (listap):
        sumaPonderada=0
        for contador, digit in enumerate(posicionList,1): #Enumerate()
            sumaPonderada += int(contador)* int(digit)#Hace la suma de la multipliccion entre el contador y el digito
        answer.append(sumaPonderada)#Agrega resultado a la lista
        #print(sumaPonderada)

for linea in lineas:
    lista = [int(x) for x in linea]
    for posicion in lista:
        posicionList = list(str(posicion))#Es necesario convertir la posición en una nueva lista
        WeightedSum(posicionList)#Se Utiliza el método
print(*answer, sep=' ')

#Forma en CodeAbbey, problema surgido: Impresion de una sola linea -_-

'''
scores = int(input())
answer=[]

def WeightedSum (listap):
        sumaPonderada=0
        for contador, digit in enumerate(posicionList,1): #Enumerate()
            sumaPonderada += int(contador)* int(digit)#Hace la suma de la multipliccion entre el contador y el digito
        answer.append(sumaPonderada)#Agrega resultado a la lista
        #print(sumaPonderada)

lista = input().split() #Imprime solo una linea

#Diferente al anterior, (ignorar un ciclo y no utilizar range())
for posicion in lista:
    posicionList = list(str(posicion))#Es necesario convertir la posición en una nueva lista
    WeightedSum(posicionList)#Se Utiliza el método
print(*answer, sep=' ')
'''

#Una forma inusual y en una sola linea :0 

'''
int(input()) and print(' '.join([str(sum(int(x[i]) * (i + 1) for i in range(len(x)))) for x in input().split()]))
'''

#utilizaron el mismo método mio -_- pero mejor 

'''
def weighted_sum_of_digits(n):
    return sum([int(ch)*(i+1) for i, ch in enumerate(str(n))])

n = int(raw_input())
l = raw_input().split()

for i in l:
    print weighted_sum_of_digits(int(i)),
'''