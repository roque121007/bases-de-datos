@app.get("/personas")
def obtener_personas():
    try:
        df = pd.read_excel("base_de_datos.xlsx", header=None)
        
        # Buscar índice de "Datos Tutorado"
        index = df[df[0] == "Datos Tutorado"].index[0]
        columnas = df.iloc[index + 1]
        datos = df.iloc[index + 2:]
        datos = datos.dropna(how="all")  # eliminar filas vacías
        datos.columns = columnas
        datos = datos[datos.columns.dropna()]  # eliminar columnas vacías
        return {"personas": datos.to_dict(orient="records")}

    except Exception as e:
        return {"error": str(e)}
