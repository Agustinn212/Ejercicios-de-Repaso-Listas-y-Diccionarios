def DiccionarioDeFrecuencias(lista_palabras):
    
    frecuencias = {}
    for palabra in lista_palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

ListaPalabras = ['manzana', 'banana', 'manzana', 'pera', 'banana', 'manzana', 'uva', 'pera',]
resultado = DiccionarioDeFrecuencias(ListaPalabras)
print(resultado) 
