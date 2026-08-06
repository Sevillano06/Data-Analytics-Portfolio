import os
from analyze_logs import analizar_dataframe

# Configurar rutas absolutas para evitar errores en la terminal
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(directorio_actual, "..", "dataset", "auth_logs.csv")
ruta_reporte = os.path.join(directorio_actual, "..", "results", "report.txt")

# Ejecutar la función importada
print("[*] Iniciando análisis de logs...")
total, fallidos, exitosos, usuarios, ips = analizar_dataframe(ruta_csv)

# Generar el archivo report.txt
print("[*] Generando reporte...")
with open(ruta_reporte, "w") as archivo:
    archivo.write("CYBERSECURITY LOG ANALYTICS REPORT\n")
    archivo.write("="*35 + "\n\n")
    
    archivo.write(f"Total logs: {total}\n\n")
    
    archivo.write(f"Failed logins:\n{fallidos}\n\n")
    archivo.write(f"Successful logins:\n{exitosos}\n\n")
    
    archivo.write("Top users:\n")
    for usuario, cantidad in usuarios.items():
        archivo.write(f"- {usuario} ({cantidad} intentos)\n")
        
    archivo.write("\nTop IP:\n")
    for ip, cantidad in ips.items():
        archivo.write(f"- {ip} ({cantidad} intentos)\n")

print(f"[+] ¡Éxito! Reporte guardado en: {ruta_reporte}")