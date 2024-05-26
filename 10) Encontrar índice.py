def EncontrarIndice(lista, valor):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            return i
        i += 1
    return -1

numeros = [1, 5, 7, 34, 5, 9, 3, 15, 11, 2, 6]
valor = 3
indice = EncontrarIndice(numeros, valor)
if indice != -1:
    print("El valor", valor, "aparece por primera vez en el índice:", indice)
else:
    print("El valor", valor, "no está presente en la lista.")
