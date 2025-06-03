from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/personas")
def obtener_personas():
    try:
        df = pd.read_excel("base_de_datos.xlsx")
        return {"personas": df.to_dict(orient="records")}
    except Exception as e:
        return {"error": str(e)}
