"""
Ejercicio 6.5 Toma el c´odigo en Python siguiente, que almacena una cadena:‘
cad = 'X-DSPAM-Confidence: 0.8475'
Usa find y rebanado de cadenas (slicing) para extraer la porci ´on de la cadena
despu´es del car´acter punto, y luego usa la funci ´on float para convertir la cadena
extra´ıda en un n´umero en punto flotante.

 """
str = 'X-DSPAM-Confidence: 0.8475'
atpos = str.find(':')
var = str[atpos+1:]
var = float(var)
print('This s a floating point number %f.' % (var))
