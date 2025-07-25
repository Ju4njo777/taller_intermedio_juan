# Búsqueda con while-else
# Dada la lista [4, 8, 15, 16, 23, 42], pide al usuario un número a buscar.

# Recorre la lista con un while y, si lo encuentras, muestra su índice y haz break.

# Si terminas el bucle sin encontrarlo, el bloque else debe imprimir “Número no encontrado”.

lista = [4, 8, 15, 16, 23, 42]
num = int(input("Ingresa un número a buscar: "))

i = 0
encontrado = False

while i < 6:  
    if lista[i] == num:
        print("Número encontrado en la posición", i)
        encontrado = True
        break
    i += 1

if not encontrado:
    print("Número no encontrado")
