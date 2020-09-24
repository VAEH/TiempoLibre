#Supongamos que se nos dan dos fechas - por ejemplo, cuando el tren o el 
# barco transbordador inician su viaje y cuando lo termina.
# tenemos la curiosidad de saber cuánto tiempo (en día, horas, minutos y segundos) se gasta en viajar (quizá con el fin de escoger la opción más rápida). ¿Cómo podríamos lograrlo?

#Una de las maneras más fáciles es:

#convierte ambas fechas a números grandes, representando los segundos desde el inicio del mes (o año, o siglo);
#calcula sus diferencias - ej.: tiempo de viaje en segundos;
#convierte esta diferencia de nuevo a días, horas, minutos y segundos.
#La primera operación podría ser realizada multiplicando los minutos por 60 y las horas por 60*60, etc. y sumando todos los valores que resulten.
#La tercera operación debería ser realizada a lo contrario, mediante varias divisiones que preserven los residuos.

#Se convierte todo a segundos, se hace la diferencia de ambos dias
#Luego se pasa nuevamente a su formato original utilizando modulo
#y la division
try:
    with open('RetosCodeAbbey/ModuloTDifference.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []

for linea in lineas:
    d1,h1,m1,s1,d2,h2,m2,s2 = [int(x) for x in linea]
    
    if s2 >=s1:
        s = s2- s1
    else: 
        m2-=1
        s2+=60
        s = s2-s1
    if m2>=m1:
        m=m2-m1
    else: 
        h2-=1
        m2+=60
        m = m2-m1
    if h2>=h1:
        h = h2-h1
    else:
        d2-=1
        h2+=24
        h = h2-h1
    d = d2 -d1
    answer.append('('+str(d)+' '+str(h)+' '+str(m)+' '+str(s)+') ')
print(' '.join(answer))

#Forma en como lo especificaba CodeAabbey que era utilizando la opcion de Modulo

'''
for i in range ( int ( input ( ) ) ):
    d1,h1,m1,s1,d2,h2,m2,s2 = input ( ).split ( " " )
    diffD = int ( d2 ) - int ( d1 ) #Resto Dias
    diffH = int ( h2 ) - int ( h1 ) #Resto Horas
    diffM = int ( m2 ) - int ( m1 ) #Resto Minutos
    diffS = int ( s2 ) - int ( s1 ) #Resto Segundos
    
    diff = diffD * 86400 + diffH * 3600 + diffM * 60 + diffS #Multiplicación de los tres
    diffD = diff / 86400 #Division diferencia por dias en segundos
    diffH = ( diff % 86400 ) / 3600 
    diffM = ( diff % 3600 ) / 60
    diffS = diff % 60
    
    print ( "(%i %i %i %i) " % ( diffD, diffH, diffM, diffS ) )
    
'''

#Una forma Más acertada a la solucion 

'''
def func():
    count = int(input())
    for i in range(count):
        input_data = input().split()
        t = list(map(int, input_data))
        a1 = t[0]*24*60*60+t[1]*60*60+t[2]*60+t[3]
        a2 = t[4]*24*60*60+t[5]*60*60+t[6]*60+t[7]
        res = a2-a1
        s = res%60
        m = res%(60*60)//60
        h = res%(24*60*60)//(60*60)
        d = res//(24*60*60)
        a = "({0} {1} {2} {3})".format(d, h, m, s)
        print(a, " ")
        
func()
'''


#Otra forma, utilizando una funcion

'''
def to_seconds(d, h, m, s):
    return ((24 * d + h) * 60 + m) * 60 + s
    
def from_seconds(sec):
    s = str(sec % 60)
    sec //= 60
    m = str(sec % 60)
    sec //= 60
    h = str(sec % 24)
    sec //= 24
    d = str(sec)
    return '(' + ' '.join([d, h, m, s]) + ')'
    
count = int(input())
results = []
for i in range(count):
    d1, h1, m1, s1, d2, h2, m2, s2 = input().split()
    d1, h1, m1, s1, d2, h2, m2, s2 = int(d1), int(h1), int(m1), int(s1), int(d2), int(h2), int(m2), int(s2)
    res = from_seconds(to_seconds(d2, h2, m2, s2) - to_seconds(d1, h1, m1, s1))
    results.append(res)
print(' '.join(results))
'''