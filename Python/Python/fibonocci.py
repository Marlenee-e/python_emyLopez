def fibonacci(n):
    fibo_series = [0, 1]
    for _ in range(n - 2): 
        fibo_series.append(fibo_series[-1] + fibo_series[-2])
    return fibo_series[:n] 

n = int(input("Ingresa la cantidad de números de Fibonacci que deseas ver: "))
print(fibonacci(n))

#Numeros paress
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [num for num in numeros if num % 2 == 0]

print("Números pares:", pares)

