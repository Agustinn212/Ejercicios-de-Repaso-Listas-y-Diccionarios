def ContarPalabras(frases):
    FrecuenciaPalabras = {}
    
    for frase in frases:
        palabras = frase.split()
        for palabra in palabras:
            if palabra in FrecuenciaPalabras:
                FrecuenciaPalabras[palabra] += 1
            else:
                FrecuenciaPalabras[palabra] = 1
    
    return FrecuenciaPalabras

frases = [
    "hola gente",
    "hola a todos",
    "muy buenas a todos"
]

frecuencias = ContarPalabras(frases)
print(frecuencias)
