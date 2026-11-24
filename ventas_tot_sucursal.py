import pandas as pd

ventas = pd.read_csv("ventas.csv")
sucursales = pd.read_csv("sucursales.csv")

# Crear columna total
ventas["total"] = ventas["precio"] * ventas["cantidad"]

# Unir con sucursales
df = ventas.merge(sucursales, on="ciudad", how="left")

# Agrupar por sucursal y sumar el total
resultado = df.groupby("sucursal")["total"].sum().reset_index()

print(resultado)