from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API funcionando. Visita /personas para obtener los datos."}

@app.get("/personas")
def obtener_personas():
    try:
        df = pd.read_excel("base_de_datos.xlsx")
        return {"Reporte de Monitoreo de Asignaciones de Tutores y Tutorados ": df.to_dict(orient="records")}
    except Exception as e:
        return {"error": str(e)}
