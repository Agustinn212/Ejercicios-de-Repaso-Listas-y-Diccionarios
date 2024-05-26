def ContarLetras(cadena):
    frecuencia = {}
    for letra in cadena:
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
    return frecuencia

cadena = "Hola Gente"
resultado = ContarLetras(cadena)
print("Frecuencia de letras:", resultado)
