estudiantes = {
    "Juan": {"edad": 20, "curso": "Python", "promedio": 8.5},
    "María": {"edad": 22, "curso": "Java", "promedio": 9.0},
    "Pedro": {"edad": 21, "curso": "Python", "promedio": 7.8},
    "Luis": {"edad": 23, "curso": "JavaScript", "promedio": 8.7}

}

estudiantes["Juan"]["promedio"] = 9.0

estudiantes_python = {nombre: datos for nombre, datos in estudiantes.items() if datos["curso"] == "Python"}

promedio_edad = sum(estudiante["edad"] for estudiante in estudiantes.values()) / len(estudiantes)

print("Estudiantes:", estudiantes)
print("Estudiantes de Python:", estudiantes_python)
print("Promedio de edad de los estudiantes:", promedio_edad)
