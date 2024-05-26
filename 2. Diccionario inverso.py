def InvertirDiccionario(diccionario):
    DiccionarioInvertido = {valor: clave for clave, valor in diccionario.items()}
    return DiccionarioInvertido

diccionario = {'a': 1, 'b': 2, 'c': 3}
DiccionarioInvertido = InvertirDiccionario(diccionario)
print(DiccionarioInvertido)  