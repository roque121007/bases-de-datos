from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Carga el archivo Excel con encabezados reales en la fila 6 (índice 5)
try:
    df = pd.read_excel("reporte_monitoreo.xlsx", header=5)
except Exception as e:
    df = None
    print(f"Error al cargar el archivo: {e}")

@app.get("/")
def root():
    return {"mensaje": "API funcionando. Usa /tutor, /tutorado o /tutor_anterior para obtener los datos."}

@app.get("/tutor")
def datos_tutor():
    if df is None:
        return {"error": "No se pudo cargar el archivo Excel"}
    columnas_tutor = [
        "DA", "Número de empleado", "Correo Institucional", "Nombre",
        "Ap Paterno", "Ap Materno", "Género", "Edad",
        "Estatus del tutor: Activo / Inactivo", "Tipo tutor / PTC / PHL",
        "Cantidad de tutorados / en el periodo activo"
    ]
    try:
        return {"datos_tutor": df[columnas_tutor].to_dict(orient="records")}
    except KeyError as e:
        return {"error": f"Columna no encontrada: {str(e)}"}

@app.get("/tutor_anterior")
def datos_tutor_anterior():
    if df is None:
        return {"error": "No se pudo cargar el archivo Excel"}
    columnas_tutor_anterior = [
        "Número de empleado", "Nombre", "Ap Paterno", "Ap Materno"
    ]
    try:
        return {"datos_tutor_anterior": df[columnas_tutor_anterior].to_dict(orient="records")}
    except KeyError as e:
        return {"error": f"Columna no encontrada: {str(e)}"}

@app.get("/tutorado")
def datos_tutorado():
    if df is None:
        return {"error": "No se pudo cargar el archivo Excel"}
    columnas_tutorado = [
        "Matrícula", "Tipo de tutorado / Nuevo ingreso (puro) - Seguimiento (reingreso)",
        "Inscrito (ficha pagada) / No inscrito (Ficha pendiente de pago)",
        "Nombre", "Paterno", "Materno", "Programa educativo", "Grado", "Género", "Edad", "Egreso",
        "Estatus de la situación de la tutoría / Solo si fue reasignado con un nuevo tutor"
    ]
    try:
        return {"datos_tutorado": df[columnas_tutorado].to_dict(orient="records")}
    except KeyError as e:
        return {"error": f"Columna no encontrada: {str(e)}"}
