def decimal_a_binario_recursivo(n):
    # Caso base
    if n < 2:
        return str(n)
    else:
        # Llamada recursiva y concatenación del resto
        return decimal_a_binario_recursivo(n // 2) + str(n % 2)

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

    resultado = decimal_a_binario_recursivo(numero)
    resultado2 = decimal_a_binario_iterativo(numero)
    
    # Mostrar el resultado usando ambas funciones
    print(f"El número {numero} en binario (recursivo) es: {resultado}")
    print(f"El número {numero} en binario (iterativo) es: {resultado2}")
