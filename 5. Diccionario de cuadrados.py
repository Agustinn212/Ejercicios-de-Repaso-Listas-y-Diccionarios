def DiccionarioDeCuadrados(n):

    return {i: i**2 for i in range(1, n + 1)}
n = 8
resultado = DiccionarioDeCuadrados(n)
print(resultado) 
