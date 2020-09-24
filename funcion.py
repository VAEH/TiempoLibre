#Ejercicio que muestra la utilizaciòn de una funcion con argumentos para el calculo de una asignaciòn de pago
#

def computepay(h,r):
        if h < 40 :
            pago = h*r
        elif h>40:
            #hrsResi = float((hrs - 40))
            pago = (40* tasa) + (hrs-40)*(tasa*1.5)       
        return pago

hrs = float(input("Enter Hours: "))
tasa = float(input("Enter Tasa: "))
p = computepay(hrs,tasa)
print("Pay",p)