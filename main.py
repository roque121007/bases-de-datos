from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API funcionando. Visita /personas para obtener los datos."}

@app.get("/personas")
def obtener_personas():
    try:
        df = pd.read_excel("base_de_datos.xlsx", sheet_name=0, header=None)  # leer sin encabezado
        secciones = {}
        current_section = None
        current_data = []

        for index, row in df.iterrows():
            first_cell = str(row[0]).strip() if not pd.isna(row[0]) else ""

            # Detectar títulos
            if first_cell == "Datos Tutor" or first_cell == "Datos Tutorado" or first_cell == "Datos Tutor anterior":
                # Guardar sección anterior si hay
                if current_section and current_data:
                    secciones[current_section] = pd.DataFrame(current_data[1:], columns=current_data[0]).to_dict(orient="records")
                    current_data = []
                current_section = first_cell
            elif current_section:
                # Agregar fila a sección actual
                current_data.append(row.tolist())

        # Guardar la última sección
        if current_section and current_data:
            secciones[current_section] = pd.DataFrame(current_data[1:], columns=current_data[0]).to_dict(orient="records")

        return secciones

    except Exception as e:
        return {"error": str(e)}
