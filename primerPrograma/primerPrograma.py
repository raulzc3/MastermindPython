# Mi primer programa en Python!
# Este programa recibe tres números como input por parte del usuario e indica los números mayor y menor

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
num3 = int(input("Introduce otro número (este será el último): "))

maxNum = max(num1, num2, num3)
minNum = min(num1, num2, num3)

print("El número mayor es ", maxNum, " y el menor es ", minNum)