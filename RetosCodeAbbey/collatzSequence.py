#Forma para saber si un número es par o impar, donde si es par, en algún se va
# a Convertir en 1 y el objetivo era contar las veces que se demoraba para
#Llegara ese valor, entonce se utilizo el ciclo While para hacerlo 

try:
    with open('RetosCodeAbbey/collatzSequence.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []

def collatzS(valor):
    contador =0
    while valor!=1: #toma nuevamente el valor del resultado hasta que sea 1
        if (valor%2)==0:
            valor = valor/2 #Valor es par
        else:
            valor= 3 * valor + 1 #valor es impar
        contador+=1
    return contador


for linea in lineas:
    lista = [int(x) for x in linea]
    for digito in lista:
        answer.append(collatzS(digito))
    print(*answer, sep= " ")

#Forma en como se publico en CodeAbbey
'''
scores = int(input())

answer=[]

lista = input().split()
def collatzS(valor):
    contador =0
    while valor!=1:
        if (valor%2)==0:
            valor = valor/2 #Valor es par
        else:
            valor= 3 * valor + 1 #valor es impar
        contador+=1
    return contador
    
for digito in lista:
    answer.append(collatzS(int(digito)))
print(*answer, sep= " ")
'''