class IMC:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def clasificar_imc(self):
        try:
            imc = self.calcular_imc()
            if imc < 18.5:
                return "Bajo peso"
            elif 18.5 <= imc <= 24.9:
                return "Peso normal"
            elif 25 <= imc <= 29.9:
                return "Sobrepeso"
            else:
                return "Obesidad"
        except ZeroDivisionError:
            return "Error: La altura no puede ser cero."
