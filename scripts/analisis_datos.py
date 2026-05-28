import pandas as pd
import matplotlib.pyplot as plt
import os

def ejecutar_analisis():
    # Carga de datos con rutas relativas obligatorias
    path_datos = os.path.join("datos", "dataset.csv")
    df = pd.read_csv(path_datos)
    
    # Adaptación robusta para procesar los registros históricos del dataset
    df['Year'] = pd.to_numeric(df['Year'])
    df['Value'] = pd.to_numeric(df['Value'])
    
    # Extraemos indicadores analíticos simulando el volumen comercial histórico
    valor_total = df['Value'].sum()
    registro_maximo = df.loc[df['Value'].idxmax()]
    
    # Exportar reporte formal de texto estructurado a /resultados
    os.makedirs("resultados", exist_ok=True)
    with open(os.path.join("resultados", "indicadores.txt"), "w", encoding="utf-8") as f:
        f.write("--- REPORTE DE RENDIMIENTO ANALÍTICO COMERCIAL ---\n")
        f.write(f"Suma Total de Registros: {valor_total:,}\n")
        f.write(f"Periodo con Mayor Indice de Actividad: {registro_maximo['Year']} (Monto: {registro_maximo['Value']:,})\n")
        
    # Generación y guardado automático de la visualización descriptiva requerida
    plt.figure(figsize=(8, 4))
    df_agrupado = df.groupby('Year')['Value'].sum().tail(15)  # Tomamos los últimos 15 períodos históricos
    df_agrupado.plot(kind='bar', color='darkblue', edgecolor='black')
    plt.title('Evolucion Temporal de Registros por Periodo')
    plt.xlabel('Periodo (Anual)')
    plt.ylabel('Volumen Acumulado')
    plt.tight_layout()
    plt.savefig(os.path.join("resultados", "grafico_resultados.png"))
    plt.close()
    print("📊 Procesamiento interno de Python finalizado con éxito.")

if __name__ == "__main__":
    ejecutar_analisis()
