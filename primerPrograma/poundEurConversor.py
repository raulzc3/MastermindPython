# Programa que convierte libras a euros, solicitando al usuario la cantidad de libras y el cambio actual

pounds = float(input("Introduce la cantidad de libras que quieres convertir: "))
change = float(input("Introduce el valor actual de las libras en euros: "))
eur = pounds * change

print("{gbp} libras = {eur} euros".format(gbp=pounds, eur=eur))
