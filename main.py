from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Permitir CORS (para que Flutter lo consuma sin problemas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/personas")
def leer_personas():
    try:
        df = pd.read_excel("base_de_datos.xlsx")  # Asegúrate que este archivo exista
        personas = df.to_dict(orient="records")
        return {"personas": personas}
    except Exception as e:
        return {"error": str(e)}
