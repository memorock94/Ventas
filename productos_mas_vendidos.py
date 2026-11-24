import pandas as pd

ventas = pd.read_csv("ventas.csv")
sucursales = pd.read_csv("sucursales.csv")

top_productos = ventas.groupby("producto")["cantidad"].sum().reset_index()
top_productos = top_productos.sort_values("cantidad", ascending=False).head(3)

print(top_productos)