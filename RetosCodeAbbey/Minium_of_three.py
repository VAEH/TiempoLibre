#Ejercicio Minium of Three de la parte de retos de CodeAbbey
#El programa ingresa a un file txt que contiene diferentes números,
#Recorre y convierte a una lista cada linea, luego se convierte a una lista tipo INT
# y luego se encuentra el minimo, nuevamente se convierte a un tipo  string

#Mí versión
def miniumofthree():
    try:
        scores = open("prueba.txt", "r")
        print('exito!')
    except:
        print("Prueba fallida")
    c = []
    for line in scores:
        splitted_line = line.split()
        #print("Estoy imprimiendo lo primero, list (str)",splitted_line)
        b=min([int(x) for x in splitted_line])
        #print('prueba nuevamente: ', b)
        c.append(b)
    prueba = " ".join(map(str, c))
    print('resultado Final: ', prueba)
miniumofthree()


#Otras Soluciones del mismo problema
'''
y=[9176392, 8042890, -9895288,
-8580052, -6941376, 6965280,
-3258957, -8081539, 652488,
9720727, -5024503, 6413919,
440977, -6578250, 5427811,
8109294, -7959968, -7377404,
3466416, -9544227, 8143329,
8505504, -9724993, -5240222,
-1547922, -3404197, -3467106,
8637161, 3923476, 3154185,
-9172383, 3099868, 1197076,
-9067671, 4519815, 4255699,
7897609, -8739142, 6174159,
-1449902, -9018414, -8850343,
-5035983, 1422563, -5428594,
-9608172, -468143, -3388563,
-6985576, -7001726, -2932790,
-8842247, -8496221, -2657783,
-4082469, -44144, 3938019,
2450424, -1406983, -2138505,
-4395390, -579366, -9038637]
z=0
x=[]

for number in y:
    while z<=62: 
        if y[z]<y[z+1] and y[z]< y[z+2]:
            x.append(y[z])
        elif y[z+1]<y[z] and y[z+1]< y[z+2]:
            x.append(y[z+1])
       
        else:
            x.append(y[z+2])
        z+=3    
print(x)  
'''

#Otra versión del mismo problema

'''
d = int(input())
j=1
listc = []
#Hasta que la variiable j no sea <= a la entrada, el programa no para y al final se agrega +1 a la variable
while j <= d:
    lista = input().split()
    mini = int(lista[0]) #Inicia en la primera posición de la lista
    for i in lista: #recorre la primer lista, al acabar agrega el minimo a la nueva lista
        if int(i) < mini: #Realiza la comparación para validar y agregar 
            mini = int(i)
    listc.append(mini)
    j = j + 1
#Convierte la lista tipo INT en tipo STR
print(' '.join(str(i) for i in listc))

'''

#Otra versión algo peculiar :v
'''
n = int(input())
sets = [map(int, input().split()) for i in range(n)]
for p in sets:
    print(min(p), end=" ")
'''

#otra versión Utilizo una especie de rebanado
'''
numbers = """-1255643 1196420 -7051267
6470816 121385 559882
8767363 -2184671 -6752906
-1483311 7837647 55023
-7419036 6418888 6175710
-5849982 -8379188 4265752
893040 -2296792 5723623
9061184 -2097377 792513
8166088 -7003229 7509232
6662211 -6694232 5013619
7512621 2050124 -3789960
-9538646 -1479059 6331425
1021236 -2711696 -5853246
4268330 5804993 -8015599
-5676646 8385957 8403289
-9500936 -7464025 -9975898
4764816 3429014 -2272691
488439 2490198 5629932
-8719047 656287 8626702
8790185 -2681502 -8067530"""

numbers = map(int, numbers.split())

col1 = numbers[0::3]
col2 = numbers[1::3]
col3 = numbers[2::3]

final = []
for j, k, l in zip(col1, col2, col3):
    if j < k and j < l:
        final.append(j)
    elif k < j and k < l:
        final.append(k)
    elif l < j and l < k:
        final.append(l)
print final
print len(final)

'''
