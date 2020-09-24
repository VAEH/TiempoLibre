try:
    with open('RetosCodeAbbey/Triangles.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        #print(lineas)
        
except:
    print("Prueba fallida")
answer = []

#En cualquier triangulo, la suma de dos de sus lados siempre
# es mayor que el tercer lado

for linea in lineas: 
    a,b,c = [int(x) for x in linea]
    if (a+b) > c and (a+c)>b and (b+c)> a :
        answer.append('1')
    else:
        answer.append('0')
print(*answer, sep=' ' )

#Forma en como se publico en Codeabbey

'''
scores = int(input())

answer=[]

for linea in range(scores):
    a,b,c = [int(x) for x in input().split()]
    if (a+b) > c and (a+c)>b and (b+c)> a :
        answer.append('1')
    else:
        answer.append('0')
print(*answer, sep=' ' )
    
'''

#Otra Solución python 2

'''
def triangle(calculatioOns):
    answer = []
    for calculation in range(calculations):
        [a,b,c] = raw_input().split()
        [a,b,c] = int(a),int(b),int(c)
        minNum = min(int(a),int(b),int(c))
        maxNum = max(int(a),int(b),int(c))

        for x in [a,b,c]:
            if int(x) != minNum and int(x) != maxNum:
                midNum = x
        a,b,c = minNum, midNum, maxNum
        if (a+b) > c:
            answer.append(str('1'))
        else:
            answer.append(str('0'))
    print(' '.join(answer))
triangle(input())
'''