def CombinarDiccionarioListas(diccionario):
    ElementosCombinados = []
    
    for lista in diccionario.values():
        ElementosCombinados += lista
    
    return ElementosCombinados

diccionario = {
    'a': [1, 2, 3],
    'b': ['hola', 'gente'],
    
}

ElementosCombinados = CombinarDiccionarioListas(diccionario)
print(ElementosCombinados)
