# Uso de break y continue
# Escribe un programa con while True que recorra números de 1 en adelante y:

# Use continue para saltar e imprimir solo los números que no sean múltiplos de 3.

# Detenga el bucle (break) cuando alcance el número 20.

i = 1

while True:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    if i == 20:
        break
    i += 1
