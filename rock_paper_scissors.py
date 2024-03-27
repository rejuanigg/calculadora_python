import random

a = random.randint(1, 3)
b = input("Elije tu Arma de combate ")

if a == 1:
    a = "piedra"
elif a == 2:
    a = "papel"
elif a == 3: 
    a = "tijeras"
else:  0

#EN CASO DE EMPATE

if (a == "papel", b == "papel"):
    print("Empate")
elif (a=="piedra", b== "piedra"):
    print("Empate")
elif (a=="tijera", b == "tijera"):
    print("Empate")

#GANA IA
elif (a =="tijera", b == "papel"):
    print("Gana IA")
elif (a == "piedra", b == "tijera"): 
    print("Gana IA")
elif (a == "papel", b == "piedra"):
    print("Gana IA")
#GANA PS
elif (b =="tijera", a == "papel"):
    print("Ganaste")
elif (b == "piedra", a == "tijera"): 
    print("Ganaste")
elif (b == "papel", a == "piedra"):
    print("Ganaste")
else: "0"

