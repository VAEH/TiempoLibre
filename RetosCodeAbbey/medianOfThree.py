#Ejercicio Medium of three #41 
#Esta basado es este Ejercicio: QuickSort algorithm
try:
    with open('RetosCodeAbbey/MedianOfThree.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        #print(lineas)
        
except:
    print("Prueba fallida")
answer = []

#El ejercicio está correcto y ordenado, pero no cumple con el requisito
for linea in lineas:
    lista =  [int(x) for x in linea]
    lista.sort() # Ordena los números de menor a mayor
    mediana = lista[ int(((len(lista) + 1 ) / 2)-1) ] # aplica la formula de la mediana cuando son impares y busca la posicion en la lista
    answer.append(mediana)
print(*answer, sep=" ")
      
#Un algoritmo que no logro entender la parte de la suma 
'''
def median_of_three(nums):
    for i in nums:
        if sum(i>j for j in nums) == 1:
            return i
        
for i in range(int(input())):
    nums = [int(n) for n in input().split()]
    print(median_of_three(nums), end=' ')
'''
#Otro tipo de ejercicio que cumple con los requisitos de codeabbdey
#Pero sigo sin entender ñla logica
'''
def swap(x,y):
    temp = y
    y = x
    x = temp
    return x,y

i = int(input())
f = open('test.txt',mode='r')
for x in range(i):
    a,b,c = f.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a > b:
        a,b = swap(a,b)
    if b > c:
        b,c = swap(b,c)
    if a > b:
        a,b = swap(a,b)
    print(b,end=' ')
'''

#Otra Solución que Utiliza dos funciones para dar respuesta
#Pero con la condicion y parámetros de CodeAbbey,además utiliza *args
'''
def solve(data):
    count, *jobs = data.splitlines()
    answers = map(solve_job, jobs)
    return ' '.join(map(str, answers))


def solve_job(job):
    a, b, c = map(int, job.split())
    if b <= a:
        a, b = b, a
    if c <= a:
        return a
    if c <= b:
        return c
    else:
        return b
'''