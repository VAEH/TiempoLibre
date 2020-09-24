'''
    El algoritmo es sencillo: revisa todos los valores, conviértelos e imprime.
    Siendo en este caso la conversión de los dato de °F a °C y rondeados

'''

try:
    scores = open("RetosCodeAbbey/ConversionFC.txt", "r")
    print('exito!')
except:
    print("Prueba fallida")
c=[]
for linea in scores: 
    convertList = [int(x) for x in linea.split()]
    #print(convertList)
    #Necesario porque en Codeabbey el primer número significa los datos totales
    listadatos = convertList[1:]
#print('Con rebanado',listadatos)

for dato in listadatos:
    c.append(round(((5*(dato-32))/9)))
c=" ".join(map(str,c))
print(c)


#Forma en como se publico en CodeAbbey, Utilizando input()
'''
scores = input()
c=[]

convertList = [int(x) for x in scores.split()]
listadatos =convertList[1:]

for dato in listadatos:
    c.append(round((dato-32)*(5/9)))
poto=" ".join(map(str,c))
print(poto)

'''

#Forma fácil utilizando las entradas de CodeAbbey

'''
for i in input().split()[1:]:
    print(round((int(i) - 32) * (5 / 9)), " ")
'''
