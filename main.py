from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API funcionando. Visita /personas para obtener los datos."}

@app.get("/personas")
def obtener_personas():
    try:
        # Cargar todas las hojas del archivo Excel
        excel_data = pd.read_excel("base_de_datos.xlsx", sheet_name=None)

        # Convertir cada hoja a lista de diccionarios
        resultado = {}
        for nombre_hoja, df in excel_data.items():
            resultado[nombre_hoja] = df.to_dict(orient="records")

        return resultado

    except Exception as e:
        return {"error": str(e)}
