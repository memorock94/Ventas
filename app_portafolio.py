import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Mi Portafolio Crypto", layout="wide")
st.title("📊 Mi Portafolio de Criptomonedas")

# Configuración del portafolio
portafolio = {
    "bitcoin": 0.05,
    "ethereum": 1.2,
    "solana": 15,
    "cardano": 500,
    "sei-network": 1000,
}

moneda = st.sidebar.selectbox("Moneda", ["usd", "mxn"])

@st.cache_data(ttl=60)  # Cache de 60 segundos
def obtener_datos():
    ids = ",".join(portafolio.keys())
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies={moneda}&include_24hr_change=true"
    respuesta = requests.get(url)
    return respuesta.json()

datos = obtener_datos()

# Crear tabla
filas = []
total = 0

for cripto, cantidad in portafolio.items():
    if cripto in datos and moneda in datos[cripto]:
        precio = datos[cripto][moneda]
        cambio = datos[cripto].get(f"{moneda}_24h_change", 0)
        valor = precio * cantidad
        total += valor
        filas.append({
            "Cripto": cripto.upper(),
            "Cantidad": cantidad,
            "Precio": precio,
            "Valor": valor,
            "Cambio 24h (%)": round(cambio, 2)
        })
    else:
        st.warning(f"No se pudo obtener datos de: {cripto}")

df = pd.DataFrame(filas)

# Mostrar métricas
col1, col2 = st.columns(2)
col1.metric("Valor Total del Portafolio", f"${total:,.2f} {moneda.upper()}")
col2.metric("Última actualización", datetime.now().strftime("%H:%M:%S"))

# Mostrar tabla
st.subheader("Detalle del Portafolio")
st.dataframe(df.style.format({
    "Precio": "${:,.2f}",
    "Valor": "${:,.2f}"
}), use_container_width=True)

# Botón para actualizar
if st.button("🔄 Actualizar ahora"):
    st.rerun()