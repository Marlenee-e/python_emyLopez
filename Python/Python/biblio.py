from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    edad = hoy - fecha_nacimiento

    años = edad.days // 365
    meses = (edad.days % 365) // 30
    días = (edad.days % 365) % 30

    return años, meses, días

fecha_nacimiento = datetime(1981, 3, 13)
años, meses, días = calcular_edad(fecha_nacimiento)
print(f"Edad: {años} años, {meses} meses, {días} días")

##
def dias_para_proximo_cumple(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
    hoy = datetime.today()
    proximo_cumple = datetime(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)

    if proximo_cumple < hoy:
        proximo_cumple = datetime(hoy.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)

    dias_faltantes = (proximo_cumple - hoy).days
    return dias_faltantes


fecha_nacimiento = "13/03/1981"  
dias_faltantes = dias_para_proximo_cumple(fecha_nacimiento)
print(f"los días restantes para el próximo cumpleaños son: {dias_faltantes}")
