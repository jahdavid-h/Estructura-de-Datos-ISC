def decimal_a_binario_recursivo(n):
    # Caso base
    if n < 2:
        return str(n)
    else:
        # Llamada recursiva
        return decimal_a_binario_recursivo(n // 2) + str(n % 2)

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número entero: "))
resultado = decimal_a_binario_recursivo(numero)
print(f"El número {numero} en binario es: {resultado}")