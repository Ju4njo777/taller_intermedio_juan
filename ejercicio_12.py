# Validación de contraseña
# Implementa un programa que solicite una contraseña correcta (puedes fijarla en tu código)
# y permita hasta 3 intentos.

# Si el usuario acierta: imprime “¡Acceso concedido!” y termina.

# Si agota los 3 intentos: imprime “Usuario bloqueado” y termina.

contraseña_correcta = "secreto"
intentos = 0

while intentos < 3:
    contraseña = input("Ingresa la contraseña: ")
    if contraseña == contraseña_correcta:
        print("¡Acceso concedido!")
        break
    intentos += 1

if intentos == 3:
    print("Usuario bloqueado")
