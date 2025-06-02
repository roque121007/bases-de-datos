from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/datos")
def obtener_datos():
    df = pd.read_excel("plantilla_base_de_datos.xlsx")
    return df.to_dict(orient="records")
