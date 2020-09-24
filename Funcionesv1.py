##Realiza el mismo ejercicio pasado, respecto a la evaluación de unos valores
#Pero la verdad toma los posibles valores dentro de una matriz
"""
Escriba un programa que solicite repetidamente a un usuario números enteros hasta
que el usuario ingrese 'hecho'. Una vez que se ingresa 'hecho', imprima el número
más grande y el más pequeño. Si el usuario ingresa algo que no sea un número válido, 
agárrelo con un try / except y envíe un mensaje apropiado e ignore el número. Ingrese 7, 2,
bob, 10 y 4 y coincida con la salida a continuación.

"""

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break 
    try:
        inp=float(num)
    except:
        print("Invalid input")
        continue

for value in [7,2,10,4]: 
    if largest is None:
        largest = value
    elif value>largest:  
        largest=value
        print("Maximum is", largest)            
for value in [7,2,10,4]: 
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest=value          
        print("Minimum is", smallest)