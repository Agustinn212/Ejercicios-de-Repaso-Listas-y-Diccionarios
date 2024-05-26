def IntercambiarValores(diccionario, clave1, clave2):

    if clave1 in diccionario and clave2 in diccionario:
        diccionario[clave1], diccionario[clave2] = diccionario[clave2], diccionario[clave1]
    return diccionario

DiccionarioOriginal = {
    'a': 1,
    'b': 2,
    'c': 3
}

clave1 = 'a'
clave2 = 'c'

DiccionarioModificado = IntercambiarValores(DiccionarioOriginal, clave1, clave2)
print(DiccionarioModificado) 