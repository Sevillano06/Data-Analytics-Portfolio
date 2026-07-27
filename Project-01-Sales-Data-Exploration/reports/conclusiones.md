# Conclusiones Iniciales (Fase de Exploración)

Tras completar el Análisis Exploratorio de Datos (EDA) inicial del dataset de ventas minoristas, destaco las siguientes observaciones clave:

1. **Calidad de los datos:** El dataset es altamente consistente. Las columnas financieras (`Price per Unit` y `Total Amount`) no presentan valores nulos, lo que facilitará la fase de análisis sin necesidad de imputar muchos datos.
2. **Distribución demográfica:** A través de las variables `Gender` y `Age`, se observa una oportunidad clara para segmentar a los clientes y entender qué grupo demográfico tiene el mayor ticket promedio de compra.
3. **Rendimiento de productos:** Utilizando filtros básicos, se identificó preliminarmente que la categoría [Escribe aquí una categoría que hayas visto que se repite mucho, ej. 'Electronics'] tiene una alta frecuencia de aparición en las transacciones.
4. **Próximas acciones de limpieza:** Se requiere estandarizar el formato de la columna `Date` para asegurar que las futuras extracciones de mes y año (para análisis de estacionalidad) funcionen correctamente.