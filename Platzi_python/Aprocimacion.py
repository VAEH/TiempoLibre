
objetivo = int(input('Escoge un numero: '))
epsilon = 0.01 #Que tan preciso queremos ser 
paso = epsilon**2 #Que tanto nos vamos acercar en cada iteración
respuesta = 0.0

#abs (regresa el valor absuluto)
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <=objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo ) >= epsilon:
    print(f'No s encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

