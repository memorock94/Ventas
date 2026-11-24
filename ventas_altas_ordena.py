import pandas as pd

ventas = pd.read_csv("ventas.csv")
sucursales = pd.read_csv("sucursales.csv")

ventas["total"] = ventas["precio"] * ventas["cantidad"]

ventas_altas = ventas[ventas["total"] > 5000]
ventas_altas = ventas_altas.sort_values("total", ascending=False)

print(ventas_altas)