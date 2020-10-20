'''
Ordenamiento es reorganizar acorde a alguna regla simple basada en la comparación. Suponte que tenemos el siguiente arreglo:
a = [3, 1, 4, 1, 5, 9, 2, 6]

y queremos que sus elementos sean reordenados en un orden no decreciente -Es decir, si un elemento es puesto primero (a la izquierda) de otro elemento - podemos estar seguros que el primer elemento es menor o igual que el segundo.

Hablando matematicamente, para algunos indices 'i' y 'j' si 'i<j' entonces a[i] <= a[j].

**Ordenamiento de burbuja ** es uno de los metodos más simples para desarrollar un reordenamiento. Nosotros describiremos esto de manera más simple que la usual:

    Toma un valor de "pase", examinando todos los pares de elementos adyacentes (pares "N-1" para el array de elementos "N").
    Si para cualquier par con índices i ei + 1 la condición a [i] <= a [i + 1] no se cumple, intercambia estos dos elementos.
    Repita dichas pasadas a través de la matriz hasta que la nueva pasada no realice cambios en absoluto.

Resulta obvio, que si el "pase" no desarrolla ningun intercambio, el array está ordenado y los pases futuros no cambiarán nada.

Para intercambiar los elementos con indices í´ e ´j´ hay algunas variantes. Por ejemplo la variable temporal 't' puede ser usada:

t = a[i]
a[i] = a[j]
a[j] = t

PROBLEMA:
Vamos a implementar la versión descrita del ordenamiento de burbuja. Para testear esto, verificaremos el numero de pases y el numero de intercambios hechos antes de que el arreglo esté ordenado.

Datos de entrada contendran el tamaño del array en la primera linea y el array en la segunda (valores enteros separados por espacios). Respuesta debe contener dos valores - numero de pases desarrollados y el total de numeros de intercabios.

podemos advertir que el numero de intercambios es aproximadamente proporcional a N^2 donde 'N' es el tamaño del array (promedio es cerca de N^2 / 4) así que el tiempo que toma el algoritmo crece significativamente más rapido que el numero de datos (por eso es que este ordenamiento es usado raramente para arrays grandes)

'''




import math 

try:
    with open('RetosCodeAbbey/SortBubble.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:] #Obvia la primer linea
        print('Exito!')
        
except:
    print("Prueba fallida")

for linea in lineas:
    lista = [int(x) for x in linea]
    #tamaño = len(lista)
j = 1 #Posición
contador = 1
prueba = 1
#El rango es (tamaño de la lista -1) porque va hacer la última posición de "j", de lo contrario generaria un error al compara la ultima posición con una posición de j que no existe
for i in range(len(lista)-1):
    prueba+=1 #Cuenta el número de intercambios que se realizaron
    #print(i)
    #Realiza la comparación de ambas posiciones, luego modifica las posiciones de la lista
    #Para que al mismo tiempo que se compara realice el ordenamiento
    if lista[i] > lista[j] : 
        #Las tres lineas posteriores modifican la lista
        t = lista[i] #variable temporal
        lista[i] = lista[j] #posición "i" toma el valor de la posición "j"
        lista[j] = t #Toma el valor temporal
        j+=1 #Incremeta 1 para la nueva posición
        contador+=1
    else: #Incrementa 1 para la nueva posición
        j+=1
print(str(contador), str(round( (prueba**2)/4) )) # Imprime número de pases desarrollados y total de intercambios
