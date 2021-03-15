# Test en el que le mostraremos al usuario sus sistema operativo ideal en base a sus respuestas
# Este test es ficción, cualquier parecido con la realidad es pura coincidencia


title = "¡Bienvenido al test de sistemas operativos!"

print("\n" + title + "\n" + "-"*len(title))

score = 0

# Primera pregunta
option = input("1.- ¿Te montarías tu propio equipo?\n"
               "     A.- Sin dudarlo.\n"
               "     B.- Preferiría que ya viniera todo montado.\n"
               "     C.- ¿Equipo de qué, de fútbol?\n")

if option == "A":
    score += 10
elif option == "B":
    score += 5
elif option == "C":
    score += 0
else:
    print("{} no es una opción válida".format(option))
    exit()

# Segunda pregunta
option = input("1.- ¿Te gusta personalizar tus entornos de trabajo?\n"
               "     A.- Claro, me gusta personalizar hasta el tipo de letra de mi reloj.\n"
               "     B.- Sin más, no es algo que me preocupe demasiado.\n"
               "     C.- Mi entorno de trabajo está perfecto según viene, no tengo que retocar nada\n")

if option == "A":
    score += 10
elif option == "B":
    score += 5
elif option == "C":
    score += 0
else:
    print("{} no es una opción válida".format(option))
    exit()

# Tercera pregunta
option = input("1.- ¿Te gusta profundizar en el funcionamiento de un ordenador?\n"
               "     A.- Por supuesto, me encanta saber que hay detrás de cada click.\n"
               "     B.- Me da curiosidad, pero mientras todo funcione correctamente no suelo involucrarme.\n"
               "     C.- Soy más de profundizar en los likes de mi último post de instagram\n")

if option == "A":
    score += 10
elif option == "B":
    score += 5
elif option == "C":
    score += 0
else:
    print("{} no es una opción válida".format(option))
    exit()

#Resultado
if score >= 25:
    result = "Linux"
elif score >= 15:
    result = "Windows"
else:
    result = "Mac"

print("Tu puntuación es {}, por lo tanto tu sistema operativo ideal es: {}".format(score, result))