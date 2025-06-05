from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API activa"}

@app.get("/tutores")
def leer_tutores():
    try:
        df = pd.read_excel("Base_de_datos_tutor.xlsx")  # Asegúrate que este archivo esté en el root
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
