lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)

#inserta
lista.insert(0, 0)
print(lista)

#elimina
lista.remove(3)
print(lista)

#ordena
lista_ordenada = sorted(lista)
print(lista_ordenada)

#nueva lista
duplicados = []
for elemento in lista:
    duplicados.extend([elemento] * 2)
print(duplicados)


#numero mayor

numeros = [23, 54, 12, 87, 32, 45, 98, 76]
maximo = max(numeros)
segundo_mas_grande = max(n for n in numeros if n != maximo)

print("El segundo número más grande es:", segundo_mas_grande)
