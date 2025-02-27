class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}"

    def fecha_cumples(self):
        self.edad += 1

    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

i = Persona("Rosa", 25, "Calle 104")
print(i)
i.fecha_cumples()
i.cambiar_direccion("4ta poniente")
print(i)


#cambiar curso
class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion)
        self.curso = curso

    def cambiar_a_curso(self, nuevo_curso):
        self.curso = nuevo_curso

    def __str__(self):
        return f"{super().__str__()}, Curso: {self.curso}"


e = Estudiante("Emilia", 20, "Calle Poniente", "Matemáticas")
print(e)
e.cambiar_a_curso("Física")
print(e)

