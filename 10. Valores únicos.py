def ValoresUnicos(diccionario):
    
    valores = diccionario.values()
    ValoresUnicos = list(set(valores))
    return ValoresUnicos

diccionario = {
    'a': 1,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 3,
    'f': 4
}

resultado = ValoresUnicos(diccionario)
print(resultado) 
