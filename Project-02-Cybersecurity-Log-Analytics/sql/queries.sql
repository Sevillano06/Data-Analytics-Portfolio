-- 1. Ver todos los registros
SELECT * 
FROM auth_logs;

-- 2. Identificar usuarios con más intentos (Posible fuerza bruta)
SELECT username, COUNT(*) as total
FROM auth_logs
GROUP BY username
ORDER BY total DESC;

-- 3. Filtrar únicamente los intentos fallidos
SELECT * 
FROM auth_logs
WHERE status = 'FAILED';

-- 4. Contar la cantidad de eventos por dirección IP
SELECT source_ip, COUNT(*) as total_eventos
FROM auth_logs
GROUP BY source_ip
ORDER BY total_eventos DESC;

-- 5. Filtrar autenticaciones exitosas
SELECT * 
FROM auth_logs
WHERE status = 'SUCCESS';