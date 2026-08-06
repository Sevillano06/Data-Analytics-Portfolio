import pandas as pd

def analizar_dataframe(ruta_csv):
    """Lee el CSV y extrae las métricas principales de seguridad."""
    df = pd.read_csv(ruta_csv)
    
    # Cálculos
    total_logs = len(df)
    failed_logins = len(df[df['status'] == 'FAILED'])
    success_logins = len(df[df['status'] == 'SUCCESS'])
    
    # Extraer los 3 usuarios e IPs con mayor actividad
    top_users = df['username'].value_counts().head(3)
    top_ips = df['source_ip'].value_counts().head(3)
    
    return total_logs, failed_logins, success_logins, top_users, top_ips

# Prueba local rápida (solo se ejecuta si corres este archivo directamente)
if __name__ == "__main__":
    import os
    ruta = os.path.join(os.path.dirname(__file__), "..", "dataset", "auth_logs.csv")
    print("Módulo de análisis cargado. Total de eventos:", analizar_dataframe(ruta)[0])