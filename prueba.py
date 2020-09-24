#Código Fibonacci Mediante un generador
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
for n in fibon(100000):
    print(n)
