from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "API activa"}

@app.get("/tutores")
def obtener_tutores():
    try:
        df = pd.read_excel("Base_de_datos_tutor.xlsx")  # Asegúrate de que el nombre del archivo sea correcto y esté en el mismo directorio
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
