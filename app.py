import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

def main():
    st.title("Visualización de Forecast")

    # CSV en Google Drive
    csv_url = 'https://drive.google.com/uc?id=1Lv-1RupyJ55Ip-fE1JSb7C-esOUZy__K'  
    
    # Cargar el CSV
    try:
        df = pd.read_csv(csv_url, encoding='utf-8', sep=';') 
    except Exception as e:
        st.error(f"Ocurrió un error al leer el CSV: {e}")
        return

    # Mostrar los datos cargados
    st.write("Datos cargados:")
    st.dataframe(df)

    # Verificar que las columnas necesarias estén presentes
    required_columns = ['Date', 'Predicción', 'Lower Bound', 'Upper Bound']
    if not all(column in df.columns for column in required_columns):
        st.error(f"El CSV debe contener las columnas: {', '.join(required_columns)}")
        return

    # Preparar los datos para ECharts
    dates = df['Date'].tolist()
    prediccion = df['Predicción'].tolist()
    lower_bound = df['Lower Bound'].tolist()
    upper_bound = df['Upper Bound'].tolist()

    # Configuración del gráfico de ECharts
    options = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {
                "type": "cross",
                "label": {
                    "backgroundColor": "#6a7985"
                }
            },
            "formatter": (
                "Fecha: {b}<br/>"
                "Predicción: {c0}<br/>"
                "Límite Inferior: {c1}<br/>"
                "Límite Superior: {c2}"
            )
        },
        "xAxis": {
            "type": "category",
            "data": dates,
            "boundaryGap": False,
            "name": "Fecha",
        },
        "yAxis": {
            "type": "value",
            "name": "Predicción",
        },
        "series": [
            {
                "name": "Predicción",
                "type": "line",
                "data": prediccion,
                "itemStyle": {
                    "color": "#5470C6"  # Color para la predicción
                },
                "lineStyle": {
                    "width": 3  # Grosor de la línea de la predicción
            },
            {
                "name": "Límite Inferior",
                "type": "line",
                "data": lower_bound,
                "itemStyle": {
                    "color": "#EE6666"  # Color para el límite inferior
                },
                "lineStyle": {
                    "type": "dashed",  # Línea punteada
                    "width": 1  # Grosor reducido
                },
                "symbol": "none"  # Sin marcadores
            },
            {
                "name": "Límite Superior",
                "type": "line",
                "data": upper_bound,
                "itemStyle": {
                    "color": "#91CC75"  # Color más claro para el límite superior
                },
                "lineStyle": {
                    "type": "dashed",  # Línea punteada
                    "width": 1  # Grosor reducido
                },
                "symbol": "none"  # Sin marcadores
            }
        ],
        "legend": {
            "data": ["Predicción", "Límite Inferior", "Límite Superior"],
            "top": "10%"  # Mover la leyenda hacia arriba
        },
        "dataZoom": [  # Agregar zoom interactivo
            {
                "type": "inside",
                "start": 0,
                "end": 100
            },
            {
                "type": "slider",
                "start": 0,
                "end": 100
            }
        ],
    }

    # Mostrar el gráfico con ECharts
    st_echarts(options=options, height="500px")

if __name__ == "__main__":
    main()
