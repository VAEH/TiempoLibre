#Greatest Common Divisor - Maximo Común Divisor MCD & MCM


try:
    with open('RetosCodeAbbey/MaximoComunDivisor.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:] #Obvia la primer linea
        print('Exito!')
        
except:
    print("Prueba fallida")
answer = []
for linea in lineas:
    mcd =0
    res =0
    num1,num2 = [int (x) for x in linea]
    a = max(num1, num2)
    b =min(num1, num2)
    while b!=0:
        res = b
        b = a%b
        a =res
    #Formula para calcular el MCM
    mcm = (num1*num2)/(res)
    #answer.append((res, int(mcm))) #Forma de imprimir, pero codeAbbey lo pedia sin coma por eso el otro modo
    answer.append('('+str(res)+' '+str(int(mcm))+')')
poto = " ".join(answer)
print(poto)

#Forma en como se publico en CodeAbbey 
'''
scores = int(input())
answer = []

for linea in range(scores):
    mcd =0
    res =0
    num1,num2 = [int (x) for x in input().split()]
    a = max(num1, num2)
    b =min(num1, num2)
    while b!=0:
        res = b
        b = a%b
        a =res
    #Formula para calcular el MCM
    mcm = (num1*num2)/(res)
    #aux = (mcd, mcm)
    answer.append('('+str(res)+' '+str(int(mcm))+')') #Append() solo recibe un argumento, por eso la forma de guardar el dato, ya que agregamos son dos    #print(answer)
poto = " ".join(answer)
print(poto)
'''


#Otra forma de realizar el ejercicio utilizando métodos para mcm & mcd
'''
def lcm(a,b): # Least Common Multiple
        return(a * b / gcd(a, b))
        
def gcd(a,b): # Greatest Common Divisor
        while b:      
                a, b = b, a % b
        return a

def findDivisors(pairs):
        answer = []
        for pair in range(int(pairs)):
                a,b = input().split()
                a,b = int(a), int(b)
                answer.append('('+str(int(gcd(a,b)))+' '+str(int(lcm(a,b)))+')')
        print(' '.join(answer))
findDivisors(input())
'''