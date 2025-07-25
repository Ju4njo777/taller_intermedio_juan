# Contador de vocales
# Solicita al usuario una palabra y, con un for,
# cuenta cuántas vocales (a, e, i, o, u) contiene. Muestra el total al final.

palabra = input("Escribe una palabra: ")
contador = 0
for letra in palabra:
    if letra.lower() in "aeiou":
        contador += 1
print("La palabra tiene", contador, "vocal(es).")
