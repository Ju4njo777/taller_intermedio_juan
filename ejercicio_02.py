# Suma acumulada (primeros 100 números)
# Implementa un programa que use un bucle for y un
# acumulador para calcular la suma de los 100 primeros
# números naturales (del 1 al 100) y muestre el resultado.


suma = 0

for numero in range(1, 101):
    suma += numero

print("La suma total es:", suma)


