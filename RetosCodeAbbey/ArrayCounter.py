#Ejercicio que se encarga de contar la frecuencia de un 
#Número en un Array y devuelve la cántidad de veces en las
#Que aparece. Se utilizo Count() y Set()
# Donde este último entrega el objeto sin repetir
# Los que aparen sin repetir :p 

try:
    with open('RetosCodeAbbey/ArrayCounter.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []

for linea in lineas:
    lista = [int(x) for x in linea]
    x = [lista.count(x) for x in set(lista)]
    x = " ".join(map(str, x))
    print(x)
            
#Una forma
'''
input1 = input()
liststr = input1.split()
listint = list(map(int,liststr))
listint.sort()
unique = list(set(listint))
empty=[]
for i in unique:
    empty.append(listint.count(i))

for i in range(10):
    print(empty[i])
'''

#Esta si tiene en cuenta y utiliza un contador para hacerlo

'''
listo = []
a = raw_input().split()
b = a.sort()

def check(number, list):
    if number in list:
        return 1
    else:
        return 0
def count(i, a):
    var = 0
    for num in a:
        if num == i:
            var += 1
    return var
    
        


for i in a:
    if check(i, listo) == 0:
        print "%d " % count(i, a)
        listo.append(i)
    else:
        pass
'''