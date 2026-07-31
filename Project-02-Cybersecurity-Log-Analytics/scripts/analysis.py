import pandas as pd

# 1. Cargar los datos
print("--- Iniciando Análisis de Logs de Seguridad ---")
df = pd.read_csv("dataset/logins.csv")

# 2. Mostrar las primeras filas para verificar
print("\n[+] Primeras filas del dataset:")
print(df.head())

# 3. Analizar el estado de las autenticaciones
print("\n[+] Conteo de Estados de Autenticación:")
print(df["estado"].value_counts())

# 4. Encontrar los usuarios con más actividad (posibles anomalías)
print("\n[+] Actividad por Usuario:")
print(df["usuario"].value_counts())