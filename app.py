import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    st.title("Streamlit Plotly Demo")

    #CSV en Google Drive
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

    # Selección de columnas
    fecha_col = st.selectbox("Selecciona la columna de fecha:", df.columns)
    valor_col = st.selectbox("Selecciona la columna de valor:", df.columns)

    # Gráfico
    fig = px.line(df, x=fecha_col, y=valor_col, title='Gráfico de línea')
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
