raw_data = (11,15,111)  

'''for number in raw_data:
    wsd = 0  # Stores sum
    suma=0
    number_list = list(str(number))  # Converts the number into a list.
    print('**************',number_list)
    for i, k in enumerate(number_list):  # Enumerates each number
        print('esto es i', i, 'esto es k', k)
        wsd += (int(i+1) * int(k))  # Multiplies and adds product to wsd
        print('Imprime valor wsd: ', wsd)
        #suma +=wsd
        #print('imprime previo ', suma)
   print('***********resultado final: ', wsd)
'''

try:
    scores = open("RetosCodeAbbey/SumOfDigits.txt", "r")
    print(scores)
    #scores = scores[1:]
    print('exito!')
except:
    print("Prueba fallida")
c = []
altelist = 0
'''
for linea in scores:
    a, b, c= [int(x) for x in linea.split()]
    #lista = lista[1:]
    print(a)
'''
