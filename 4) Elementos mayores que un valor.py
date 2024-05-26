def ElementosMayoresQue(lista, n):
    resultado = []
    for num in lista:
        if num > n:
            resultado.append(num)
    return resultado

numeros = [7, 4, 4, 2, 10, 9, 2, 17, 5, 6, 1]
n = 4
resultado = ElementosMayoresQue(numeros, n)
print("Los elementos mayores que", n, "son:", resultado)
