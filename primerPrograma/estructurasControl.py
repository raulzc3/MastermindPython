# Ejercicio simple para practicar la sintaxis de un if

print("Vamos a preparar un Colacao")
print("Abrimos la nevera")

milk = input("Hay leche? (S/N): ")
colacao = input("¿Hay Colacao? (S/N): ")

if milk != "S" or colacao != "S":
    print("Vamos a comprar al super...")
    if milk != "S":
        print("Compro leche")
    if colacao != "S":
        print("Compro colacao")

print("Añadimos leche a un vaso, agragamos colacao, removemos y a disfrutar!")
