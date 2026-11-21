import pandas as pd

# Leer el CSV
df = pd.read_csv("ventas.csv")
print("Datos originales:")
print(df.head())

# Crear una columna nueva (total)
df["total"] = df["precio"] * df["cantidad"]

# Filtrar solo productos de CDMX
df_cdmx = df[df["ciudad"] == "CDMX"]

# Guardar resultado
df.to_csv("ventas_procesadas.csv", index=False)
print("\nArchivo guardado correctamente")