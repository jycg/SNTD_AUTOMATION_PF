import random
from faker import Faker

# Definir la función para reemplazar vocales con caracteres especiales
def reemplazar_vocales(cadena, transformar):
    # Diccionario de vocales y sus posibles reemplazos
    reemplazos = {
        'A': ['Á', 'Ä', '-', '.', 'Ñ'],
        'E': ['É', 'Ë', '-', '.', 'Ñ'],
        'I': ['Í', 'Ï', '-', '.', 'Ñ'],
        'O': ['Ó', 'Ö', '-', '.', 'Ñ'],
        'U': ['Ú', 'Ü', '-', '.', 'Ñ'],
        'a': ['Á', 'Ä', '-', '.', 'Ñ'],
        'e': ['É', 'Ë', '-', '.', 'Ñ'],
        'i': ['Í', 'Ï', '-', '.', 'Ñ'],
        'o': ['Ó', 'Ö', '-', '.', 'Ñ'],
        'u': ['Ú', 'Ü', '-', '.', 'Ñ']
    }

    # Función para reemplazar una vocal con un carácter especial aleatorio
    def reemplazar_caracter(c):
        if c in reemplazos:
            return random.choice(reemplazos[c])
        return c

    # Generar la nueva cadena con reemplazos si transformar es 2
    if transformar == 2:
        nueva_cadena = ''.join(reemplazar_caracter(c) for c in cadena)
    else:
        nueva_cadena = cadena

    return nueva_cadena.upper()


# Crear instancias de Faker
fake = Faker()

# Obtener datos falsos
nombre_p = fake.first_name()
nombre_s = fake.first_name()
apellido_p = fake.last_name()
apellido_s = fake.last_name()


# Generar un número de teléfono en el formato deseado
def generar_telefono(tipo_telefono):
    if tipo_telefono == 1:
        return f"331-698-{random.randint(1000, 9999)}"
    else:
        return f"101-{random.randint(100, 999)}-{random.randint(1000, 9999)}"


# Parámetro para controlar la transformación de vocales
transformar = 2
# 1 - Datos faker sin caracteres especiales
# 2 - Datos faker con caracteres especiales
# 3 - Datos reales

# Parámetro para controlar el tipo de teléfono
tipo_telefono = 2
# 1 - Teléfono "real"
# 2 - Teléfono Faker

# Concatenar los nombres con un espacio en blanco entre ellos
entrada_nombre_p = f"{nombre_p}"
entrada_nombre_s = f"{nombre_s}"
entrada_apellido_p = f"{apellido_p}"
entrada_apellido_s = f"{apellido_s}"

# Aplicar la función de reemplazo de vocales
if transformar == 3:
    nombre_p_transformado = "JULIO"
    nombre_s_transformado = "DE JESÚS"
    apellido_p_transformado = "GARCÍA"
    apellido_s_transformado = "HERNÁNDEZ"
else:
    nombre_p_transformado = reemplazar_vocales(entrada_nombre_p, transformar)
    nombre_s_transformado = reemplazar_vocales(entrada_nombre_s, transformar)
    apellido_p_transformado = reemplazar_vocales(entrada_apellido_p, transformar)
    apellido_s_transformado = reemplazar_vocales(entrada_apellido_s, transformar)

# Generar el número de teléfono
celular = generar_telefono(tipo_telefono)

# Obtener el email falso
email = fake.email()

# Crear la cadena de JavaScript
js_code = f"""
document.getElementById("txtfName").value = "{nombre_p_transformado}";
document.getElementById("txtsName").value = "{nombre_s_transformado}";
document.getElementById("txtflastName").value = "{apellido_p_transformado}";
document.getElementById("txtsLastName").value = "{apellido_s_transformado}";
document.getElementById("txtCelphone").value = "{celular}";
document.getElementById("cboPhoneCompany").value = "8";
document.getElementById("txtMail").value = "{email}";
"""

# Mostrar el resultado
print(js_code)
