#a persistencia del residuo sobre la adición y la multiplicación. Esta importante propiedad es a menudo usada para verificar los resultados de los cálculos, en las competencias 
# de programación, en los cálculos de sumas de verificación (checksums) y especialmente para el cifrado.
#Tenemos aquí una especie de cálculo aritmético extenso, y se nos pide el módulo del resultado con otro número
#La Respuesta debería dar el residuo del resultado de todas las operaciones aplicadas secuencialmente (empezando por el número inicial) y dividido entre el último número.
try:
    with open('RetosCodeAbbey/ModularCalculator.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        #lineas = lineas[1:]
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []
#resultado =0

for pru in lineas[:1]: #Coge el primer dato, y que este no contiene signo y generaria error pal método siguiente
    a =int(''.join(map(str, pru)))
    print(a)
resultado = a
    #print(''.join(pru))
#print(numero)
for linea in lineas[1:]: #Ignora el primwer dato
    signo, digito = [x for x in linea]
    #print(digito)
    #Realiza validación de signo para la operación
    if signo == '+':
        resultado = int(resultado)+ (int(digito))
    if signo == '*':
        resultado = int(resultado )* (int(digito))
        #resultado %= resultado 
    if signo == '%': #realiza el modulo de la operación 
        resultado %= int(digito)   
print(str(resultado)) 

#Otras soluciones
'''
def modCalc(num):
        calc = raw_input()
        while calc[:1] != "%":
                if calc[:1] == '+':
                        num += int(calc[2:].strip())
                elif calc[:1] == '*':
                        num *= int(calc[2:].strip())
                calc = raw_input()
        num %= int(calc[2:].strip()) 
        print(num)
modCalc(input())
'''

#Otra forma

'''
n = int(input()) #Toma el primer dato que no contiene signo
do = input().split() #realiza el split
while do[0] != '%': #realiza operación hasta que se encuentre con el Modulo
    k = do[0] #Se orienta el primer posicoón donde esta el signo
    if (k == '+'):
        n += int(do[1])
    else:
        n *= int(do[1])
    do = input().split()
print(n%int(do[1])
'''

#Ottra forma utilizanod booleanos

'''
result = int(input())

calc = []

while True:
    line = input().split()
    operator = line[0]
    value = int(line[1])
    
    if operator == '%':
        division = value
        break
    
    calc.append({'operator': operator, 'value': value})

for e in calc:
    if e['operator'] == '+':
        result += e['value']
    elif e['operator'] == '*':
        result *= e['value']
    result = result % division

print(result)
'''