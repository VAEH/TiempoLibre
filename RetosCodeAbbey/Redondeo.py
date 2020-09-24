'''
    Hay varios pares de números. Para cada par, debe dividir primero por 
    segundo y devolver el resultado, redondeado al entero más cercano. En los casos, 
    cuando el resultado contiene exactamente 0.5 como fracción, el valor debe redondearse 
    hacia arriba.

    Hay una formula de redondeo cuando es exacto a 0.5 y es: -[-(x)-o.5] creo que es redondeo hacia arriba

    Se hace la division de los dos numeros, el resultado se separa por ENTERO y otro DECIMAL con el método .modf()
    con condionales se hizo la validacion tanto si se era positivo como negativo (Comparando el decimal con 0.5 y siguiendo la regla correspondiente)
'''
#Habia otro método que era utilizar el método .roud()
#Forma en un Archivo de texto
import math 
try:
    scores = open("RetosCodeAbbey/Redondeo.txt", "r")
    print('exito!')
except:
    print("Prueba fallida")
c = []
altelist = 0
for linea in scores:
    prueba = [float(x) for x in linea.split()]
    division = (prueba[0] / prueba[1])
    decimal, entero = math.modf(division)
    if decimal >0:
        if decimal < 0.5:
            altelist = (entero)
        if decimal > 0.5:
            altelist = (entero+1)
        elif decimal == 0.5:
            altelist = (-(-(division)-0.5))
    elif decimal == 0.0:
        altelist = (entero)
    else: 
        if decimal > -0.5:
            altelist = (entero)
        if decimal < -0.5:
            altelist = (entero-1)
        elif decimal == -0.5:
            altelist = (-(-(division)-0.5))
    c.append(int(altelist))
poto=" ".join(map(str,c))
#print(altelist)
print(poto)

#Forma cogiendo una entrada (input())
#La misma baina, p.d.: Se me olvido pegar el código jejjeje pero estas son otras soluciones
#Mí código pero utilizando la función round()
'''
import math 
try:
    scores = open("RetosCodeAbbey/Redondeo.txt", "r")
    print('exito!')
except:
    print("Prueba fallida")
c = []
altelist = 0
for linea in scores:
    prueba = [float(x) for x in linea.split()]
    division = round((prueba[0] / prueba[1]))
    c.append(int(division))
poto=" ".join(map(str,c))
#print(altelist)
print(poto)

'''

#Otra solución
'''
hasil = ""
for i in range(int(input())):
    data = input().split()
    for a in range(len(data)):
        data[a] = int(data[a])
    hasil += str(round(data[0]/data[1])) + " "
print(hasil)
'''

#Otra Solución que se asemeja a como lo estaba pensando en un inicio
#Buen pensado jajajaja

'''
n=int(input())
print()
for i in range(n):
    a,b=map(int, input().split())
    r1 = a/b
    r2 = a//b
    if r1-r2>=0.5 :
        print(r2+1,end=' ')
    else :
        print(r2, end=' ')
'''