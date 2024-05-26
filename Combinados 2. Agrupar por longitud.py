def AgruparPorLongitud(palabras):
    LongitudPalabras = {}
    
    for palabra in palabras:
        longitud = len(palabra)
        if longitud in LongitudPalabras:
            LongitudPalabras[longitud].append(palabra)
        else:
            LongitudPalabras[longitud] = [palabra]
    
    return LongitudPalabras

palabras = [
    "hola", "todos", "a", "gente", "dicen", "hola", "están", "como"
]

agrupadas = AgruparPorLongitud(palabras)
print(agrupadas)
