def decimal_a_binario_iterativo(n):
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario  # Agregar el resto al inicio
        n //= 2  # División entera
    
    return binario

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número entero: "))
resultado = decimal_a_binario_iterativo(numero)
print(f"El número {numero} en binario es: {resultado}")