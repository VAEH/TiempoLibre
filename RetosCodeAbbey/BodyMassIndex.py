
try:
    with open('RetosCodeAbbey/BodyMassIndex.txt', 'r') as f:
        lineas= [linea.split() for linea in f]
        lineas = lineas[1:]
        #print(lineas)
        
except:
    print("Prueba fallida")
answer = []


#entradaDatos()
#Método que calcula el BMI (Indice de masa corporal)
#Recibe peso y altura como parametro
def BodyMassIndex(peso, altura):
    bmi= ((peso)/altura**2) #Fomrula
    #print('esto es:  ',bmi)
    #Ciclo dice a que categoria pertenece e imprime resultado
    if bmi < 18.5:
        result = 'Under'
    if  bmi>= 18.5 and bmi <25.0:
        result='normal'
    if  bmi>=25.0 and bmi <30.0:
        result='over'
    if bmi>=30.0:
        result='obese'
    return result

#BodyMassIndex()
#BodyMassIndex(58,1.65)
#Ciclo que recorre la linea
for linea in lineas:
    peso, altura = [float(x) for x in  linea] #Divide la categoria en P, A
    #print(peso, altura)
    #Llamá al método BMI y le pasa Peso y Altura como argumentos e imprim
    answer.append(BodyMassIndex(peso, altura))
print(*answer, sep=' ' )
    #Pas
    #print(peso, peso)

#Publicacion en CodeAbbey

'''
scores = int(input())
answer = []
def BodyMassIndex(peso, altura):
    bmi= ((peso)/altura**2) #Fomrula
    if bmi < 18.5:
        result = 'Under'
    if  bmi>= 18.5 and bmi <25.0:
        result='normal'
    if  bmi>=25.0 and bmi <30.0:
        result='over'
    if bmi>=30.0:
        result='obese'
    return result

for linea in range(scores):
    peso, altura = [float(x) for x in  input().split()]
    answer.append(BodyMassIndex(peso, altura))
print(*answer, sep=' ' )
'''

#No hubo necesidad de agregar otra solcuión, todas eran similares