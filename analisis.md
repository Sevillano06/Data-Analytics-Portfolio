# Análisis Exploratorio de Datos (EDA) - Ventas de Retail

En esta fase de exploración inicial, se ha examinado la estructura general, consistencia y calidad del archivo `dataset.xlsx`.

## 1. Estructura General del Dataset

- **Cantidad de Registros (Filas):** 1000 filas
- **Cantidad de Variables (Columnas):** 9 columnas.

### Diccionario de Datos Inicial:
- **Transaction ID:** Identificador único de la transacción (Numérico/Clave).
- **Date:** Fecha en la que se realizó la compra (Temporal).
- **Customer ID:** Identificador único del cliente (Alfanumérico/Clave).
- **Gender:** Género del cliente: Male / Female (Categórica).
- **Age:** Edad del cliente en años (Numérica discreta).
- **Product Category:** Categoría del producto adquirido (Categórica).
- **Quantity:** Cantidad de unidades adquiridas (Numérica entera).
- **Price per Unit:** Precio unitario del producto (Numérica continua).
- **Total Amount:** Monto total de la transacción, calculado como Quantity * Price per Unit (Numérica continua).

## 2. Diagnóstico de Calidad de Datos

Tras la inspección ocular y la aplicación de fórmulas de diagnóstico en Excel, se determinaron los siguientes hallazgos:

- **Datos Faltantes (Nulos):** No se  detectaron valores nulos en ningunos de las columnas claves
- **Registros Duplicados:** No se encontraron IDs de trasaccion duplicados  
- **Formato y Tipos de Datos:**
  - Las columnas de montos financieros (`Price per Unit` y `Total Amount`) están configuradas como [moneda / número general].
  - Las fechas en la columna `Date` presentan un formato consistente DD/MM/AAAA.

## 3. Observaciones Relevantes
- La variable `Age` nos permitirá segmentar el comportamiento de compra por grupos generacionales en fases posteriores.
- El campo `Gender` está estandarizado sin errores de escritura evidentes (como variaciones de mayúsculas o espacios adicionales).