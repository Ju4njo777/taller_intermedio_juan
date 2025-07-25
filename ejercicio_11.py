# Suma hasta cero
# Crea un programa que lea números del usuario repetidamente con while hasta que ingrese un 0. Al finalizar,
# muestra la suma de todos los valores ingresados (excluyendo el cero).

suma = 0
num = int(input("Ingresa un número (0 para terminar): "))

while num != 0:
    suma += num
    num = int(input("Ingresa un número (0 para terminar): "))

print("La suma total es:", suma)
