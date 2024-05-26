def ContarElementos(lista, valor):
    contador = 0
    for num in lista:
        if num == valor:
            contador += 1
    return contador

numeros = [2, 5, 4, 1, 5, 8, 2, 2, 5, 1, 5]
valor = 5
resultado = ContarElementos(numeros, valor)
print("El valor", valor, "aparece", resultado, "veces en la lista.")
