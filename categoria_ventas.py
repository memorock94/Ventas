import pandas as pd

ventas = pd.read_csv("ventas.csv")
sucursales = pd.read_csv("sucursales.csv")

ventas["total"] = ventas["precio"] * ventas["cantidad"]

def categorizar(total):
    if total > 10000:
        return "Alta"
    elif total >= 3000:
        return "Media"
    else:
        return "Baja"

ventas["categoria"] = ventas["total"].apply(categorizar)
print(ventas)