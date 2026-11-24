import pandas as pd

ventas = pd.read_csv("ventas.csv")
sucursales = pd.read_csv("sucursales.csv")



df = ventas.merge(sucursales, on="ciudad", how="left")
df["total"] = df["precio"] * df["cantidad"]

resultado = df.groupby(["ciudad", "gerente"])["total"].sum().reset_index()
print(resultado)