#Se utilizo nuevo método para abrir ficheros "with"  desde mi perspectiva manteniene la integridad del archivo
try:
    with open('RetosCodeAbbey/SumOfDigits.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        
except:
    print("Prueba fallida")
answer = []
#https://www.codeabbey.com/index/wiki/number-to-digits Link con la info
#Existe un problema y es que coge el rango que nos da CodeAbbey y no lo ignora
for linea in lineas:
    a,b,c = linea[0], linea[1], linea[2] #Selecciona los 2 datos que existe dentro de lista
    formula = list(str((int(a) * int(b)) + int(c)))#Aplica la formula que codeAbbey dio y se convierte a lista
    suma =0
    for numero in formula:
        suma += int(numero)  #Recorre la lista y se suman dichos números
    answer.append(suma)
poto=" ".join(map(str,answer)) # Se convierte a tipo string
print(poto)


#Forma en como "YO" lo estaba pensando antes de entrar crisis :v
# Pero lo hizo otro man, pero cogiendo la entrada   
'''
n = int(input())
stdinput = []

for i in range(n):
    stdinput.append(list(map(int, input().split())))

ans = []
    
for num_set in stdinput:
    digits = []

    num = (num_set[0] * num_set[1]) + num_set[2]

    quo = 1

    while quo != 0:
        quo = int(num / 10)
        rem = num % 10
        digits.append(rem)
        num = quo

    ans.append(sum(digits))
    quo = 1

print(*ans, sep=" ")
'''

#Otra forma, utilizando un split para la separacion de los dogitos
#Además de utilizar el residuo % y un while
'''
n = int(input())
for _ in range(n):
    a, b, c = [int(x) for x in input().split()]
    sumd, t = 0, a * b + c
    while t > 0:
        sumd += t % 10
        t //= 10
    print(sumd, end=" ")
print()
'''