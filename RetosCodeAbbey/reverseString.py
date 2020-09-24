#Reversa de una cadena
#En mi caso, utilice ciclos y contadores para coger la posicion
#Otros utilizaron la opción de rebanado
#Que por cierto, es mucho más fácil -_- [::-1]

#Anexo link con más info: https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
try:
    with open('RetosCodeAbbey/reverseString.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        #lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []
newlist=[]
pareverse = []
for linea in lineas:
    tamaño = len(linea)#Tamaño lista principal
    for x in range(tamaño):#recorre la lista e imprime de atras hacia adelante
        newlist.append(linea[tamaño-1]) 
        tamaño -= 1
    for palabra in newlist:#Recorre posiciones de lista principal
        tamañoPala= len(palabra)#Tamaño de cada palabra
        sumaLetra = ''
        for y in palabra:#Recorre palabra, por cada uno de sus componentes y lo imprime de atras hacia adelante
            sumaLetra += palabra[tamañoPala-1]
            tamañoPala-=1
        answer.append(sumaLetra)#Agrega a matriz
    respuesta = ' '.join(map(str, answer))#Imprime
    print(respuesta)

#Publicación CodeAbbey

'''
lineas = input().split()
answer = []
newlist=[]
pareverse = []
tamaño = len(lineas)
for x in range(tamaño):
    newlist.append(lineas[tamaño-1])
    tamaño -= 1
for palabra in newlist:
    tamañoPala= len(palabra)
    sumaLetra = ''
    for y in palabra:
        sumaLetra += palabra[tamañoPala-1]
        tamañoPala-=1
    answer.append(sumaLetra)
respuesta = ' '.join(map(str, answer))
print(respuesta)
'''

#La forma más facil y que no me percate jajajajja
'''
string = str(input()) [::-1]
print(string)
'''