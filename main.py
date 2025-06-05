from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "API activa"}

@app.get("/datos-tutor")
def obtener_datos():
    df = pd.read_excel("Base_de_datos_tutor.xlsx")  # Asegúrate de que el archivo esté en el mismo directorio
    return df.to_dict(orient="records")
