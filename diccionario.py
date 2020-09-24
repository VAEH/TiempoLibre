try:
    archivo = open('mbox-short.txt','r')
    print('exito')
except:
    print('fallo')
'''    
listaDias = []
dicciDias = {}
for linea in archivo:
    listaDias = linea.split()
    if len(listaDias)>3 and linea.startswith('From '):
        dia = listaDias[2]
        #print(dia)
        if dia not in dicciDias:
            dicciDias[dia]= 1
        else:
            dicciDias[dia]+=1
print(dicciDias)
'''
'''
correDic={}
listaCorre=[]

for linea in archivo:
    listaCorre = linea.split()
    if linea.startswith('From '):
        correo = listaCorre[1]
        if correo not in correDic:
            correDic[correo]=1
        else:
            correDic[correo]+=1
print(correDic)
'''   


