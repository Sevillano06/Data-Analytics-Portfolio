import pandas as pd

# 1. Cargar el dataset real
# Intentamos cargar desde la carpeta notebooks o desde la raíz
try:
    df = pd.read_csv('../data/retail_sales_dataset.csv')
except FileNotFoundError:
    df = pd.read_csv('data/retail_sales_dataset.csv')

print("=== Análisis Exploratorio Inicial: Retail Sales ===\n")

# Pregunta 1: ¿De qué tamaño es nuestro dataset?
filas, columnas = df.shape
print(f"1. Tamaño del dataset: {filas} filas y {columnas} columnas.\n")

# Pregunta 2: ¿Qué columnas tenemos y qué tipo de datos son?
print("2. Tipos de datos por columna:")
print(df.dtypes)
print("\n")

# Pregunta 3: ¿Hay datos faltantes (nulos) que debamos limpiar?
print("3. Cantidad de valores nulos por columna:")
print(df.isnull().sum())
print("\n")

# Pregunta 4: Estadísticas básicas (promedio, mínimo, máximo de las columnas numéricas)
print("4. Resumen estadístico de valores numéricos:")
print(df.describe())
print("\n")

# Vista previa de las primeras 3 filas para entender el contexto
print("5. Vista previa de los datos (primeras 3 filas):")
print(df.head(3))