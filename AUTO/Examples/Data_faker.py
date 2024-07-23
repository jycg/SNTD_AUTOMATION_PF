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
def obtener_datos_falsos():
    nombre_p = fake.first_name()
    nombre_s = fake.first_name()
    apellido_p = fake.last_name()
    apellido_s = fake.last_name()
    return nombre_p, nombre_s, apellido_p, apellido_s


# Generar un número de teléfono en el formato deseado
def generar_telefono(tipo_telefono):
    if tipo_telefono == 1:
        return f"331-698-{random.randint(1000, 9999)}"
    else:
        return f"101-{random.randint(100, 999)}-{random.randint(1000, 9999)}"


# Función para obtener y validar la selección del usuario
def obtener_seleccion(mensaje, opciones):
    while True:
        try:
            seleccion = input(mensaje)
            if seleccion.lower() == "exit":
                return seleccion.lower()
            seleccion = int(seleccion)
            if seleccion in opciones:
                return seleccion
            else:
                print(f"Por favor, ingrese un número válido: {opciones}")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def main():
    try:
        while True:
            # Pedir al usuario seleccionar los valores de "transformar" y "tipo_telefono"
            print("Seleccione el tipo de transformación de vocales:")
            print("1 - Datos faker sin caracteres especiales")
            print("2 - Datos faker con caracteres especiales")
            print("3 - Datos reales")
            transformar = obtener_seleccion("Ingrese el número correspondiente (1, 2, 3) o escriba 'exit' para salir: ", [1, 2, 3])
            if transformar == "exit":
                break

            print("\nSeleccione el tipo de teléfono:")
            print("1 - Teléfono 'real'")
            print("2 - Teléfono Faker")
            tipo_telefono = obtener_seleccion("Ingrese el número correspondiente (1, 2) o escriba 'exit' para salir: ", [1, 2])
            if tipo_telefono == "exit":
                break

            # Obtener datos falsos
            nombre_p, nombre_s, apellido_p, apellido_s = obtener_datos_falsos()

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
            print("\n" + "=" * 50 + "\n")
    except Exception as e:
        print(f"Se ha producido un error: {e}")


if __name__ == "__main__":
    main()
