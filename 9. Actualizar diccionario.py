def ActualizarDiccionario(diccionario, ListaDuplas):
   
    for clave, valor in ListaDuplas:
        diccionario[clave] = valor
    return diccionario

DiccionarioOriginal = {
    'a': 1,
    'b': 2,
    'c': 3
}

ListaDuplas = [('a', 10), ('d', 4), ('c', 5)]

DiccionarioActualizado = ActualizarDiccionario(DiccionarioOriginal, ListaDuplas)
print(DiccionarioActualizado) 
