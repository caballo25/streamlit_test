import streamlit as st
import plotly.express as px
import pandas as pd

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

    # Gráfico de línea con intervalos de confianza
    fig = px.line(df, x='Date', y='Predicción', title='Forecast con Intervalos de Confianza')
    
    # Añadir intervalos de confianza
    fig.add_scatter(
        x=df['Date'], 
        y=df['Lower Bound'], 
        mode='lines', 
        line=dict(color='rgba(0,100,80,0.2)'), 
        name='Límite Inferior'
    )
    fig.add_scatter(
        x=df['Date'], 
        y=df['Upper Bound'], 
        mode='lines', 
        line=dict(color='rgba(0,100,80,0.2)'), 
        fill='tonexty',  # Rellenar el área entre las líneas
        name='Límite Superior'
    )

    # Personalizar el gráfico
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='Predicción',
        hovermode='x unified'  # Muestra información al pasar el mouse
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)

    # Gráfico de área (opcional)
    st.write("### Gráfico de Área")
    fig_area = px.area(df, x='Date', y='Predicción', title='Forecast con Intervalos de Confianza (Área)')
    fig_area.add_scatter(
        x=df['Date'], 
        y=df['Lower Bound'], 
        mode='lines', 
        line=dict(color='rgba(0,100,80,0.2)'), 
        name='Límite Inferior'
    )
    fig_area.add_scatter(
        x=df['Date'], 
        y=df['Upper Bound'], 
        mode='lines', 
        line=dict(color='rgba(0,100,80,0.2)'), 
        fill='tonexty',  # Rellenar el área entre las líneas
        name='Límite Superior'
    )
    st.plotly_chart(fig_area)

if __name__ == "__main__":
    main()
