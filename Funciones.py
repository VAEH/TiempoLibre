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
    try:
        num = input("Enter a number: ")
        if num == "done" : break
        num = int(num)
        #print(num)
    
        
        if largest is None or largest>num:
            largest=num
        elif smallest is None or smallest <num:
            smallest=num
    except: 
        print('Invalid input')

print ("Minium", smallest)
print("Maximum", largest)