# Análisis Exploratorio Inicial

Durante la primera revisión del dataset utilizando Microsoft Excel, se documentaron las siguientes características estructurales:

* **Número de filas:** 1000 registros de ventas.
* **Número de columnas:** 9 variables de análisis.
* **Variables numéricas:** Age, Quantity, Price per Unit, Total Amount.
* **Variables categóricas:** Transaction ID, Date, Customer ID, Gender, Product Category.
* **Valores vacíos:** Tras aplicar filtros rápidos en Excel, no se identificaron celdas en blanco en las variables críticas de ingresos o cantidad.
* **Registros duplicados:** No se encontraron filas idénticas ni identificadores de transacción (Transaction ID) repetidos.
* **Calidad de datos:** Los datos presentan un formato tabular limpio. Se identificó la necesidad de validar que la columna de fechas tenga el formato correcto (DD/MM/YYYY o YYYY-MM-DD) para evitar errores en análisis de series de tiempo futuros.