import pandas as pd

# Leer archivos
ventas = pd.read_csv("ventas.csv")
sucursales = pd.read_csv("sucursales.csv")

# Crear columna total
ventas["total"] = ventas["precio"] * ventas["cantidad"]

# Unir ventas con sucursales por ciudad
resultado = ventas.merge(sucursales, on="ciudad", how="left")

# Guardar resultado
resultado.to_csv("ventas_con_sucursales.csv", index=False)

print("Archivo creado correctamente")
print(resultado.head())
