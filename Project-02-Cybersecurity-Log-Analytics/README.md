# Cybersecurity Log Analytics

## Objetivo
Analizar registros de autenticación utilizando Python y SQL para identificar patrones de comportamiento y posibles anomalías.

## Herramientas
- **Lenguajes:** Python, SQL
- **Librerías:** Pandas
- **Formatos:** CSV
- **Bases de Datos:** SQLite

## Dataset
Registros de autenticación simulados que contienen usuarios, direcciones IP y estados de conexión (SUCCESS/FAILED).

## Funciones Implementadas
- Lectura estructurada de logs.
- Detección de intentos fallidos.
- Conteo y agrupación por usuarios.
- Conteo y agrupación por direcciones IP.
- Exportación automatizada de reportes en `.txt`.

## SQL
Se desarrollaron consultas analíticas orientadas a la investigación de seguridad:
- Agrupación y conteo de eventos por usuario e IP.
- Filtrado de vectores de ataque o autenticaciones sospechosas.

## Resultados Clave
- Total de eventos analizados.
- Top de usuarios con más intentos registrados.
- Top de direcciones IP con mayor volumen de actividad.

## Futuras Mejoras (Próximas fases)
- [ ] Dashboard interactivo en Power BI.
- [ ] Gráficos automáticos generados con Python (Matplotlib).
- [ ] Automatización avanzada.
- [ ] Mapeo de hallazgos con el framework MITRE ATT&CK.