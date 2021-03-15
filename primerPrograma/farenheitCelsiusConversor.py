# Programa que convierte el input del usuario (grados Farenheit) a grados Celsius

farenheit = int(input("Introduce la temperatura en Farenheit: "))
celsius = (farenheit-32)*5/9

print("{far}ºF = {cel}ºC".format(far=farenheit, cel=celsius))
