-- Contar la cantidad de registros por usuario
SELECT usuario, COUNT(*) as total_intentos
FROM logins
GROUP BY usuario
ORDER BY total_intentos DESC;

-- Contar la cantidad de fallos vs éxitos
SELECT estado, COUNT(*) as cantidad
FROM logins
GROUP BY estado;