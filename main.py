from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "API activa"}

@app.get("/tutores")
def obtener_tutores():
    try:
        df = pd.read_excel("Base_de_datos_tutor.xlsx")  # Asegúrate del nombre exacto
        return df.to_dict(orient="records")
    except Exception as e:
        # Mostrar el error completo en el navegador
        return {"error": str(e)}
