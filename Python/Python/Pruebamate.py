import mate

try:
    print("Suma: ", mate.suma(10, 5)) 
    print("Resta: ", mate.resta(10, 5)) 
    print("Multiplicación: ", mate.multiplicacion(10, 5))  
    print("División: ", mate.division(10, 5))  
    print("Factorial de 5: ", mate.factorial(5))  
    print("Es primo 7?: ", mate.es_primo(7))  
    print("Es primo 8?: ", mate.es_primo(8))  
except Exception as e:
    print("Ocurrió un error:", e)
