#debe generar resultados (sumas de los primeros miembros) para cada secuencia,
#separados por espacios.A B N A B N N
#Ejercicio de progresiones aritmeticas: Debe calcular la suma de los primeros miembros de la secuencia aritmética
#Se utilizo nuevo método para abrir ficheros "with"  desde mi perspectiva manteniene la integridad del archivo
try:
    with open('RetosCodeAbbey/ProgresionAritmetica.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        #print(lineas)
        
except:
    print("Prueba fallida")
answer = []
#prueba = 0
for linea in lineas:
    a,b,c = [int(x) for x in linea]  #Forma de dividir los datos lista en una variable
    prueba=0
    for i in range(c): #Coge el tamaño del recorrido de C, de cada lista
        prueba += (a + (b*i))# Sumatoria del primer miembro A más el valor del incremento por el tamaño de paso
    answer.append(prueba)
print(*answer, sep=" ")  #Utiliza un *args para imprimir el resultado, junto con sep que es una especie de separador   

    
#Forma en la que se publico en CodeAbbey
#Forma simple y bonita
'''
scores = int(input())
answer = []

for linea in range(scores):
    a,b,c = [int(x) for x in input().split()]  
    prueba=0
    for i in range(c): 
        prueba += (a + (b*i))
    answer.append(prueba)
print(*answer, sep=" ")  
'''
#Otra Solución de CodeAbbey
'''
rows = int(input())

for _ in range(rows):
    a, b, n = (int(i) for i in input().split())
    s= int(a*n + b*n*(n-1)/2)
    print(s, end =' ')
'''
