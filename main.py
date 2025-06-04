from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API funcionando. Visita /personas para obtener los datos."}

@app.get("/personas")
def obtener_personas():
    try:
        df = pd.read_excel("base_de_datos.xlsx", header=None)
        
        # Buscar los índices donde aparecen los títulos
        secciones = {}
        indices = {}
        for i, row in df.iterrows():
            value = str(row[0]).strip() if not pd.isna(row[0]) else ""
            if value in ["Datos Tutor", "Datos Tutorado", "Datos Tutor anterior"]:
                indices[value] = i
        
        # Ordenar por posición en el archivo
        orden = sorted(indices.items(), key=lambda x: x[1])
        for idx, (nombre, fila_inicio) in enumerate(orden):
            fila_titulo = fila_inicio + 1
            fila_datos = fila_inicio + 2
            fila_fin = orden[idx + 1][1] if idx + 1 < len(orden) else len(df)

            df_seccion = df.iloc[fila_datos:fila_fin].copy()
            df_seccion.columns = df.iloc[fila_titulo]
            df_seccion = df_seccion.dropna(how="all")  # eliminar filas completamente vacías
            secciones[nombre] = df_seccion.to_dict(orient="records")

        return secciones

    except Exception as e:
        return {"error": str(e)}
