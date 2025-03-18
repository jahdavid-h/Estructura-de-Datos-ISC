def contar_letra_recursivo(cadena, letra):

    if not cadena:
        return 0
    
    return (1 if cadena[0] == letra else 0) + contar_letra_recursivo(cadena[1:], letra)


cadena = "La iteratividad es una técnica en programación que consiste en repetir un conjunto de instrucciones"
letra = "a"
resultado_recursivo = contar_letra_recursivo(cadena, letra)
print(f"La letra '{letra}' aparece {resultado_recursivo} veces en la cadena.")