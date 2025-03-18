def decimal_a_binario_recursivo(n):

    if n < 2:
        return str(n)
    else:
       
        return decimal_a_binario_recursivo(n // 2) + str(n % 2)

def decimal_a_binario_iterativo(n):
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2  # División entera
    
    return binario

try:
    numero = int(input("Ingrese un número entero: "))
    
    # Mostrar el resultado usando ambas funciones
    print(f"El número {numero} en binario (recursivo) es: {decimal_a_binario_recursivo(numero)}")
    print(f"El número {numero} en binario (iterativo) es: {decimal_a_binario_iterativo(numero)}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")