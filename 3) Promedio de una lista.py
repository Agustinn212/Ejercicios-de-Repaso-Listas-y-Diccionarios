def promedio(lista):
    if not lista: 
        return 0

    suma = 0
    for num in lista:
        suma += num

    return suma / len(lista)
numeros = [3, 1, 4, 1, 5, 2, 2, 6, 5, 3, 5]
resultado = promedio(numeros)
print("El promedio de los elementos es:", resultado)
