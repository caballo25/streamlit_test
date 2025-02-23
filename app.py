import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    st.title("Streamlit Plotly Demo")

    # URL del CSV en Google Drive
    csv_url = 'https://drive.google.com/uc?id=1qURQOkwzxEis7OWWvBhjuBI4VbpKIE4n'
    
    # Cargar el CSV en un DataFrame con una codificación específica
    try:
        df = pd.read_csv(csv_url, encoding='ISO-8859-1')  # Cambia la codificación si es necesario
    except Exception as e:
        st.error(f"Ocurrió un error al leer el CSV: {e}")
        return

    # Mostrar los datos cargados
    st.write("Datos cargados:")
    st.dataframe(df)

    # Selección de columnas
    fecha_col = st.selectbox("Selecciona la columna de fecha:", df.columns)
    valor_col = st.selectbox("Selecciona la columna de valor:", df.columns)

    # Gráfico
    fig = px.line(df, x=fecha_col, y=valor_col, title='Gráfico de línea')
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
