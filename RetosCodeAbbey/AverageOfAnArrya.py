#Como calcular el promedio de una lista Python
#Hay un método que se creo para elimianr el dato sin utilizar Remove
#tambíen se utiliza ciclo como contador de la posicion de datos en lista
#Utiliza map() para dividir los datos y list() para ponerlos en lista
try:
    with open('RetosCodeAbbey/AverageOfAnArray.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []

def AverageArray(suma, n):
    promedio = round( (suma / n) ) 
    answer.append(promedio)

for linea in lineas:
    lista =[int(x) for x in linea]
    lista.remove(0) #Remueve el Cero de la lista
    n = len(lista) #Cuenta el número de datos en la lista
    sumalista= sum(lista)#Suma
    AverageArray(sumalista, n)
print(*answer, sep=' ')


#Ejercicio de ejecución en CodeAbbey
'''
scores = int(input())
answer=[]

def AverageArray(suma, n):
    promedio = round( (suma / n) ) 
    answer.append(promedio)
for linea in range(scores):
    lista =[int(x) for x in input().split()]
    lista.remove(0) #Remueve el Cero de la lista
    n = len(lista) #Cuenta el número de datos en la lista
    sumalista= sum(lista)#Suma
    AverageArray(sumalista, n)
print(*answer, sep=' ')
'''
#Ejercicio Python 2, pero utilizando un método para eliminar dato
'''
#Toma la matriz, la recorre, donde esta el Cero'0', pone el dato siguiente
#Y se agrega de nuevo a la matriz, hace una especie de reemplazo
def cleanData(data):
        array = []
        for x in data:
                if x != '0' or 0:
                        array.append(x)
        return array

def average(amount):
        answer = []
        for x in range(amount):
                array = raw_input().split()
                array = cleanData(array)
                total, average, y = 0,0,0
                while y < len(array): #Para cuando sea menor a la cantidad de datos
                        total += int(array[y])
                        #utiliza el tipo Format
                        y+=1#Utiliza contador para incrementar posicion dentro de la matriz
                        average = "%.02f" % ((float(total)) / float(len(array)))
                        average = int(round(float(average)))
                answer.append(str(average))
        print(' '.join(answer))
average(input())
'''
#Otro ehercicio, utiliza map y suma de 0.5 sin necesidad de redondeo
#Porque lo hace con int()
'''
def avg( numbers ): 
       l = len(numbers) -1 
       total = 0 
       for x in numbers: 
              total = total + x 
       return int(( total / l) + 0.5) 
count = int ( input() ) 
for i in range(0,count): 
      numbers = list ( map (int, input().split() ) )
      a = avg ( numbers ) 
      print ( a ) 
      if ( i != (count-1)):
            print ( " ")
'''