import requests
import pandas as pd
from datetime import datetime
import time

portafolio ={
    "bitcoin": 0,
    "ethereum": 0,
    "solana": 0,
    "sei-network": 30000,
}

moneda = "usd"
intervalo_minutos = 1

def obtener_precios(ids):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(ids),
        "vs_currencies": moneda,
        "include_24hr_change": "true"
    }

    respuesta = requests.get(url, params=params)
    return respuesta.json()

def actualizar_portafolio():
    print(f"\n{'='*50}")
    print(f"Actualización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")

    ids = list(portafolio.keys())
    precios = obtener_precios(ids)

    registros = []
    total_portafolio = 0

    for cripto, cantidad in portafolio.items():
        if cripto in precios:
            precio = precios[cripto][moneda]
            cambio = precios[cripto].get(f"{moneda}_24h_change", 0)
            valor = precio * cantidad
            total_portafolio += valor

            print(f"{cripto.upper():<12} | Precio: ${precio:>10,.2f} | "
                  f"24h: {cambio:>6.2f}%")

            registros.append({
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "cripto": cripto,
                "precio": precio,
                "cantidad": cantidad,
                "valor": valor,
                "cambio_24h": cambio
            
            })

    print(f"\n{'TOTAL PORTAFOLIO:':<40} ${total_portafolio:,.2f} {moneda.upper()}")

    df_nuevo = pd.DataFrame(registros)
    try:
        historial = pd.read_csv("historial_portafolio.csv")
        historial = pd.concat([historial, df_nuevo], ignore_index=True)
    except FileNotFoundError:
        historial = df_nuevo

    historial.to_csv("historial_portafolio.csv", index=False)
    print("Historial guardado en historial_portafolio.csv")

actualizar_portafolio()

print(f"\nEl script se actualizará cada {intervalo_minutos} minuto. Presiona Ctrl+C para detener.")
while True:
    time.sleep(intervalo_minutos * 60)
    actualizar_portafolio()