def contar_letra_iterativo(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador


cadena = "La recursividad es una técnica en programacion donde una funcion se llama a sí misma para resolver un problema."
letra = "o"
resultado_iterativo = contar_letra_iterativo(cadena, letra)
print(f"La letra '{letra}' aparece {resultado_iterativo} veces en la cadena.")