def EliminarDuplicados(lista):
    resultado = []
    for num in lista:
        if num not in resultado:
            resultado.append(num)
    return resultado

numeros = [9, 13, 14, 4, 2, 5, 14, 7, 2, 6, 10, 3, 10]
resultado = EliminarDuplicados(numeros)
print("La lista sin números duplicados es:", resultado)
 