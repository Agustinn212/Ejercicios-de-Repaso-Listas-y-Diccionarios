def MergeDiccionarios(diccionario1, diccionario2):
    DiccionarioCombinado = diccionario1.copy()
    DiccionarioCombinado.update(diccionario2)
    return DiccionarioCombinado

diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 20, 'd': 4}
DiccionarioCombinado = MergeDiccionarios(diccionario1, diccionario2)
print(DiccionarioCombinado)  