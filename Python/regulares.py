import re

def validar_email(email):
    patron = r'^[1-8]+@[\w.-]+\.[a-zA-Z]{2,}$'  
    return bool(re.match(patron, email))

print(validar_email("123@dominio.com"))  
print(validar_email("78@empresa.net")) 
print(validar_email("usuario@dominio.com"))  
print(validar_email("9@dominio.com")) 

##
import re

def extraer_fechas(texto):
    patron = r'\b\d{2}/\d{2}/\d{4}\b'
    fechas = re.findall(patron, texto)
    return fechas

texto = "La reunión será el 15/04/2023 y la entrega será programada para el 30/05/2023."
fechas = extraer_fechas(texto)
print(fechas) 



