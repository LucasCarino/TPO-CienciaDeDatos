import fitz  # PyMuPDF
import re
import pandas as pd

def extraer_datos_pdf(ruta_pdf):
    documento = fitz.open(ruta_pdf)
    datos_extraidos = []

    # Expresiones regulares para extraer la información
    patron_nombre = re.compile(r"^Dr\.?\s\w+,\s\w+")
    patron_direccion = re.compile(r"^\d+\s?\w+\.?\s?\w+.*")  # Direcciones aproximadas
    patron_telefono = re.compile(r"(\d{2,5}-\d{3,5}-\d{3,5}|\d{2,5}-\d{3,5})")
    patron_correo = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

    for pagina in documento:
        texto = pagina.get_text("text")
        lineas = texto.split('\n')
        medico_actual = {}
        direccion_actual = ""

        for linea in lineas:
            # Verificar si la línea es un nombre de doctor
            if patron_nombre.match(linea):
                # Guardar los datos del doctor anterior
                if medico_actual:
                    if direccion_actual:
                        medico_actual["direccion"] = direccion_actual.strip()
                    datos_extraidos.append(medico_actual)
                # Nuevo doctor
                medico_actual = {"nombre": linea}
                direccion_actual = ""
                print(f"Nuevo doctor encontrado: {linea}")

            # Verificar si la línea es una dirección
            elif patron_direccion.match(linea) and not patron_telefono.search(linea):
                direccion_actual += " " + linea
                print(f"Dirección encontrada: {direccion_actual.strip()}")

            # Verificar si la línea contiene teléfonos
            telefonos = patron_telefono.findall(linea)
            if telefonos:
                medico_actual["telefono"] = ", ".join(telefonos)
                print(f"Teléfonos encontrados: {medico_actual['telefono']}")

            # Verificar si la línea contiene correos electrónicos
            correo = patron_correo.search(linea)
            if correo:
                medico_actual["correo"] = correo.group()
                print(f"Correo encontrado: {medico_actual['correo']}")

        # Agregar el último doctor después de la última página
        if medico_actual:
            if direccion_actual:
                medico_actual["direccion"] = direccion_actual.strip()
            datos_extraidos.append(medico_actual)

    documento.close()
    return datos_extraidos

# Ejemplo de uso
ruta_pdf = "../data/Cartilla.pdf"
datos_medicos = extraer_datos_pdf(ruta_pdf)

# Crear un DataFrame con los datos extraídos
df = pd.DataFrame(datos_medicos)
print(df.head())  # Ver las primeras filas

# Guardar los datos en un archivo CSV
df.to_csv("medicos_cartilla.csv", index=False)

# O en un archivo Excel
df.to_excel("medicos_cartilla.xlsx", index=False)