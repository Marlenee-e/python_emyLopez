def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero no esta permitida"
    return a / b

def factorial(n):
    if n < 0:
        return "Error: el factorial no está definido para números negativos"
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
