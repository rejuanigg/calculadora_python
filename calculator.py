# CALCULADORA
# Usar consola de python, introducí el numero X luego la operacion y por ultimo un numero Y

a = int(input("Dame a "))
o = str(input("introducí operación "))
if o == "#":
    b  = 0
else: b = int(input("Dame b "))

def suma (a, b):
    resultado = a + b 
    return resultado

def multiplier (a, b):
    resultado = a * b 
    return resultado

def divisor (a, b):
    resultado = a / b 
    return resultado

def dif (a, b):
    resultado = a - b 
    return resultado
    
def potencia (a, b):
    resultado = a ** b
    return resultado

def raiz (a):
    resultado = a ** 0.5
    return resultado 

def operacion (o):
    return
if  o == "+":
    print(suma(a, b))
elif o == "^":
    print(potencia(a, b))
elif o == "#":
    print (raiz(a))
elif o == "/":
    print ( int (divisor(a,b)))
elif o == "*" :
    print(multiplier(a,b))
elif o == "-":
    print(dif(a,b))
else: print("No introdujo una operación válida")