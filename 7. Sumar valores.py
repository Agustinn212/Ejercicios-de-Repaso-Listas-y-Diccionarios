def SumarValores(diccionario):
    
    return sum(diccionario.values())

DiccionarioNumerico = {
    'a': 9,
    'b': 8,
    'c': 4,
    'd': 9
}

resultado = SumarValores(DiccionarioNumerico)
print(resultado)  
