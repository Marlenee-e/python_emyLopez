def guardar_nombres(nombres, archivo):
    try:
        with open(archivo, 'w') as file:
            file.writelines(nombre + '\n' for nombre in nombres)
        print("Nombres guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar nombres: {e}")

def leer_nombres(archivo):
    try:
        with open(archivo, 'r') as f:
            return [linea.strip() for linea in f]
    except Exception as e:
        print(f"Error al leer nombres: {e}")
        return []

nombres = ["Adonis", "Marlene", "Esau", "Emilia"]
archivo = 'nombres.txt'

guardar_nombres(nombres, archivo)

print("Nombres leídos:", leer_nombres(archivo))

##empleados

import csv

def gestionar_empleados(archivo, empleados):
    try:
        with open(archivo, 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Nombre", "Edad", "Cargo", "Salario"])
            writer.writerows(empleados)
            f.seek(0)  # Vuelve al inicio del archivo para leerlo
        
            reader = csv.DictReader(f)
            salarios = {}
            for fila in reader:
                cargo = fila['Cargo']
                salario = int(fila['Salario'])
                salarios.setdefault(cargo, []).append(salario)
            
            print("Archivo CSV creado exitosamente.")
            for cargo, lista_salarios in salarios.items():
                print(f"Salario promedio para {cargo}: {sum(lista_salarios) / len(lista_salarios)}")

    except Exception as e:
        print(f"Error al manejar el archivo CSV: {e}")

empleados = [
    ["Adonis", 28, "Ingeniera", 5000],
    ["Emilia", 25, "Gerente", 7000],
    ["Marlene", 29, "Analista", 4500],
    ["Esau", 30, "Director", 10000]
]

gestionar_empleados('empleados.csv', empleados)

