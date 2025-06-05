from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/usuarios")
def leer_usuarios():
    try:
        df = pd.read_excel("Base_de_datos_tutor.xlsx", skiprows=2)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return {"error": "Archivo Excel no encontrado"}
    except Exception as e:
        return {"error": str(e)}

