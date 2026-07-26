# Reporte de Análisis de Ventas Retail

## 1. Preguntas de Negocio
*Para guiar este Análisis Exploratorio de Datos (EDA), he planteado las siguientes preguntas clave centradas en el comportamiento del cliente y el rendimiento del catálogo:

1. ¿Qué categoría de productos (Product Category) genera el mayor volumen de ingresos totales (Total Amount)?
2. ¿Cuál es el rango de edad de los clientes que realizan la mayor cantidad de compras?
3. ¿Existe una diferencia significativa en el ticket promedio de compra (Total Amount) entre clientes masculinos y femeninos?
4. ¿En qué fechas del registro se observa el mayor número de transacciones (Transaction ID)?
5. ¿Qué categoría de productos presenta el menor número de unidades vendidas (Quantity) por transacción?*

## 2. Exploración de los Datos
*En esta fase de exploración inicial, se ha examinado la estructura general, consistencia y calidad del archivo `dataset.xlsx`.

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
- El campo `Gender` está estandarizado sin errores de escritura evidentes (como variaciones de mayúsculas o espacios adicionales).*

## 3. Conclusiones
*Tras completar el Análisis Exploratorio de Datos (EDA) inicial del dataset de ventas minoristas, destaco las siguientes observaciones clave:

1. **Calidad de los datos:** El dataset es altamente consistente. Las columnas financieras (`Price per Unit` y `Total Amount`) no presentan valores nulos, lo que facilitará la fase de análisis sin necesidad de imputar muchos datos.
2. **Distribución demográfica:** A través de las variables `Gender` y `Age`, se observa una oportunidad clara para segmentar a los clientes y entender qué grupo demográfico tiene el mayor ticket promedio de compra.
3. **Rendimiento de productos:** Utilizando filtros básicos, se identificó preliminarmente que la categoría [Escribe aquí una categoría que hayas visto que se repite mucho, ej. 'Electronics'] tiene una alta frecuencia de aparición en las transacciones.
4. **Próximas acciones de limpieza:** Se requiere estandarizar el formato de la columna `Date` para asegurar que las futuras extracciones de mes y año (para análisis de estacionalidad) funcionen correctamente.*