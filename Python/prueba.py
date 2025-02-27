from IMC import IMC

peso = float(input("Por favor ingrese su peso en kilogramos: "))
altura = float(input("Por favor ingrese su altura en metros: "))

try:
    persona = IMC(peso, altura)
    imc = persona.calcular_imc()
    clasificacion = persona.clasificar_imc()

    print(f"Su IMC es: {imc:.1f}")
    print(f"Su clasificación es: {clasificacion}")

except ValueError as e:
    print(e) 