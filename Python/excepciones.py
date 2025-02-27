def division_segura(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: División por cero no permitida"
    except TypeError:
        return "Error:deben ingresar solo valores numéricos"
    else:
        return resultado

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Resultado:", division_segura(num1, num2))
except ValueError:
    print("Error: Deben ingresar solo valores numéricos")

    ##
class EdadInvalidaError(Exception):
  pass

def verificar_edad(edad):
    if not isinstance(edad, int) or not (0 <= edad <= 120):
        raise EdadInvalidaError("La edad debe ser un número entero entre 0 y 120 años")
    return True

try:
    edad = int(input("Ingrese su edad: "))
    verificar_edad(edad)
    print("Edad válida")
except (ValueError, EdadInvalidaError) as e:
    print(e)

