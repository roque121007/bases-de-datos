from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API para consultar usuarios. Usa /usuarios o /usuarios/{DA}"}

@app.get("/usuarios")
def leer_usuarios():
    df = pd.read_excel("Base_de_datos_tutor.xlsx", skiprows=2)  # O ajusta skiprows según tu Excel
    return df.to_dict(orient="records")

@app.get("/usuarios/{usuario_id}")
def leer_usuario(usuario_id: int):
    df = pd.read_excel("Base_de_datos_tutor.xlsx", skiprows=2)
    usuario = df[df["DA"] == usuario_id]
    if usuario.empty:
        return {"error": "Usuario no encontrado"}
    return usuario.to_dict(orient="records")[0]
