# Menú repetitivo
# Desarrolla un menú en bucle while con estas opciones:

# Sumar dos números

# Restar dos números

# Multiplicar dos números

# Salir
# Elige la opción, pide los operandos, muestra el resultado y vuelve a mostrar
# el menú hasta que seleccione “Salir”.

while True:
    print("\nMenú:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a + b)

    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a - b)

    elif opcion == "3":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", a * b)

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida, intenta de nuevo.")
