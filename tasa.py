try:
        hrs = float(input("Enter Hours:"))
        tasa = float(input("Ingrese el precio por hora: "))    
except :
    print('Sea escrito un caracter no numerico')
    quit()

print(hrs,tasa)
if hrs < 40 :
    pago = hrs*tasa
    print (pago)

elif hrs > 40: 
    hrsResi = float((hrs - 40))
    pago = (40* tasa) + hrsResi*(tasa*1.5)

print(pago) 
 #elif hrs >40: