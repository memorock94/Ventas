import requests
import pandas as pd
from datetime import datetime

url = "https://api.coingecko.com/api/v3/simple/price"
parametros = {
    "ids": "bitcoin",
    "vs_currencies": "usd,mxn",
    "include_24hr_change": "true"
}

respuesta = requests.get(url, params=parametros)
datos = respuesta.json()

#extraer información bitcoin
precio_usd = datos["bitcoin"]["usd"]
precio_mxn = datos["bitcoin"]["mxn"]
cambio_24h = datos["bitcoin"]["usd_24h_change"]
cambio_24h_mxn = datos["bitcoin"]["mxn_24h_change"]


#mostrar resultado bitcoin
print(f"Precio de Bitcoin:")
print(f"USD: ${precio_usd:,.2f}")
print(f"MXN: ${precio_mxn:,.2f}")
print(f"Cambio 24h: {cambio_24h:.2f}%")
print(f"Cambio 24h mxn: {cambio_24h_mxn:.2f}%")


#guardado en CSV
registro ={
    "fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "precio_usd": [precio_usd],
    "precio_mxn": [precio_mxn],
    "cambio_24h": [cambio_24h,],
    "cambio_24h_mxn": [cambio_24h_mxn],
}

df = pd.DataFrame(registro)

#Si el archivo ya existe, agrega nueva fila. si no, lo crea
try:
    historial = pd.read_csv("historial_bitcoin.scv")
    hitosrial = pd.concat([historial, df], ignore_index=True)
except FileNotFoundError:
    historial = df

historial.to_csv("historial_bitcoin.csv", index=False)
print("\nRegistro guardado en historial_bitcoin.csv")
