#Dada la matriz de enteros, debemos iterar a través de todos los pares de elementos vecinos, 
# comenzando desde el principio, e intercambiar los miembros de cada par en el caso de que el primer elemento sea mayor que el segundo.

#Esta operación mueve algunos elementos grandes hacia la derecha (hacía el final de la matriz) y algunos 
# elementos más pequeños hacia la izquierda (hacia el principio de la matriz).
#Lo más importante es que: el elemento más grande necesariamente se mueve a la última posición.


try:
    with open('RetosCodeAbbey/BubbleSort.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        #lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
for linea in lineas: 
    print(linea)
    lista = [int(x) for x in linea]
    tamaño = len(lista)
#print(lista)
contador =0
answer =[]
j = 1
#Método de chequeo de la suma
def checSum(array):
    result = 0
    for i in array:
        result = (result+i)*113
        result = result%10000007
    return result
    #print(result)
#Toma el tamaño y utiliza el rango para el incremento del indice en la matriz
for i in range(tamaño):
    if lista[j] !=-1: #Validación Hasta que j se encuentre con el '-1' donde termina
        #Compara posicion 1 y 2 para realizar el intercambio 
        if lista[i] >= lista[j] :
            t = lista[i]
            lista[i] = lista[j]
            lista[j] = t
            j+=1
            contador +=1
        else:
            j+=1
    else:
        lista = lista[:tamaño-1]
        break
print(lista )
print(str(contador), str(checSum(lista)))#llama a la funcion e imprime

#Como se monto en CodeAbbey, valgame dios porque casi que no

'''
lista = input().split()

tamaño = len(lista)
contador =0
answer =[]
j = 1

def checSum(array):
    result = 0
    for i in array:
        result = (result+i)*113
        result = result%10000007
    return result

for i in range(tamaño):
    if int(lista[j]) !=-1:
        if int(lista[i]) >= int(lista[j]) :
            t = lista[i]
            lista[i] = lista[j]
            lista[j] = t
            j+=1
            contador +=1
        else:
            j+=1
    else:
        lista = lista[:tamaño-1]
        break
lista = [int(x) for x in lista]
#print(lista )
print(str(contador), str(checSum(lista)))
'''

#La Forma que si era, más bonita y cortica :'v

'''
arr = list(map(int, input().split()[:-1]))


def calculate_checksum(L):
    result = 0
    for item in L:
        result += item
        result *= 113
        result %= 10000007
    return result


swaps = 0
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        swaps += 1

print(swaps, calculate_checksum(arr))
'''

#Utiliza el ciclo while, pero en este caso mientras sea True py2
'''
a=raw_input().split()
c=0
while(True):
    swap=0
    for i in range(len(a)-2):
        if int(a[i])>int(a[i+1]):
            t=a[i]
            a[i]=a[i+1]
            a[i+1]=t
            swap+=1
    if swap==0:
        break
    else:
        c+=swap
        break
i=0
result=0
for i in range(len(a)-1):
    result = ((result+int(a[i]))*113)%10000007 
print c,result
            
'''
