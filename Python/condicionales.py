num = int(input("Ingresa un número: "))

if num == 0:
    print("Cero")

elif num % 2 == 0: 
    if num > 0:
        print("Par positivo")
    else:
        print("Par negativo")
else: 
    if num > 0:
        print("Impar positivo")
    else:
        print("Impar negativo")
