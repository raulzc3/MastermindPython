# El usuario debe introducir un número, y si es el que está definido en el programa, este gana el juego
# Importamos el módulo random para poder generar números aleatorios
import random


# Generamos un entero aleatorio del 1 al 10
luckyNum = random.randint(1, 10)

print("¡Bienvenido a guess the number!")
print("Debes acertar un número del 1 al 10 como si de la lotería se tratase, ¿Estás preparado?")

userNum = int(input("¿Qué numero vas a elegir? (1-10): "))

if (1 <= userNum <= 10):
    if userNum == luckyNum:
        print("Enhorabuena, ¡Has ganado!")
    print("El número ganador es {}".format(luckyNum))
else:
    print("Vaya, veo que no has entendido el juego...")




