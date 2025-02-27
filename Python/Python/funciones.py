def suma_total(*numeros):
   return sum(numeros)

print(suma_total(1, 2, 3, 4))

#Decoradora
import time

def tiempo_ejecucion(func):
    def wrap(*args, **kwargs):
        inicio = time.time() 
        resultado = func(*args, **kwargs)
        fin = time.time() 
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
        return resultado
    return wrap


def ejemplo():
    time.sleep(2)
    print("Función ejecutada")

ejemplo()


