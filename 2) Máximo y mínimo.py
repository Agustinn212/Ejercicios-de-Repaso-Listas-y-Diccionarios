def MaximoYMinimo(lista):
    if not lista: 
        return None, None

    maximo = lista[0]
    minimo = lista[0]

    for num in lista:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

    return maximo, minimo
numeros = [3, 10, 13, 1, 5, 9, 2, 6, 0, 3, 5]
maximo, minimo = MaximoYMinimo(numeros)
print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)