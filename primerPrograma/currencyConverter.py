# Programa que permite al usuario convertir libras o dólares a euros según su elección
# NO es un conversor fiable, ya que no actualiza la tasa de cambio, es solo un ejercicio de prueba

dolar_eur = 0.84
pound_eur = 1.16

user_option = int(input("¿Qué conversión te gustaría realizar?\n"
                    "    1.- Dólares a euros\n"
                    "    2.- Euros a dólares\n" 
                    "    3.- Libras a euros\n"
                    "    4.- Euros a libras\n"
                    "Introduce una opción [1-4]: "))

if user_option == 1:
    initial_currency = "dólares"
    final_currency = "euros"
    change = dolar_eur
elif user_option == 2:
    initial_currency = "euros"
    final_currency = "dólares"
    change = 1/dolar_eur
elif user_option == 3:
    initial_currency = "libras"
    final_currency = "euros"
    change = pound_eur
elif user_option == 4:
    initial_currency = "euros"
    final_currency = "libras"
    change = 1/pound_eur
else:
    print("{} no es una opción válida".format(user_option))
    exit()


quantity = float(input("Introduce la cantidad de {} que quieres convertir a {}: ".format(initial_currency, final_currency)))
result = round(quantity * change, 2)

print("{} {} = {} {}".format(quantity, initial_currency, result, final_currency))
