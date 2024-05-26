def ProductoElementos(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

numeros = [2, 5, 8, 1, 7]
resultado = ProductoElementos(numeros)
print("El producto de los elementos es:", resultado)
