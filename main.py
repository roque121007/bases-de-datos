from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/datos")
def obtener_datos():
    df = pd.read_excel("datos.xlsx")
    return df.to_dict(orient="records")
