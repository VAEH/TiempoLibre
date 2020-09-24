
#Ejercicio de 1000 datos en un vector, numero repetido se convierte a cero y se mantiene el original, se cuenta las veces que se hizo
#Y se realiza la multiplicación 
#Falta realizar la multiplicación, excluyendo los ceros 
import random
vector = []
answer = []
for i in range(1,6):
    vector.append(random.randint(1,10))
print(vector)
#prueba = len(vector)
#print(prueba)
#print(range(prueba))

#for i in range(len(vector)):
contador = 0
for j in vector:
    if j not in answer:
        answer.insert(vector.index(j), j)
        #answer.append(j)
    #print(vector.index(j), j)
    else: 
        answer.insert(vector.index(j), 0)
        contador+=1
#answer.remove(0)
total = 0
print(answer)
#answer.remove(0)
print(contador)
        #else:
         #   answer.insert(i, 0)
#print(answer)
#            answer[i] =0
#print(answer)

