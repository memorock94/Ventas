import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
respuesta = requests.get(url)

print("Código de estado:", respuesta.status_code)

datos = respuesta.json()

df = pd.DataFrame(datos)

print("\nPrimeros registros:")
print(df.head())

df.to_csv("usuarios_api.csv", index=False)
print("\nArchivo 'usuarios_api.csv' guardado correctamente")