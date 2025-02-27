texto = "Python es un lenguaje de programación. Python es fácil de aprender."

palabras = texto.split()

frecuencia = {}

for palabra in palabras:
    
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)
