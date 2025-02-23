import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    st.title("Streamlit Plotly Demo")

    # ejem
    df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [10, 20, 25, 30, 40]
    })

    # Gráfico
    fig = px.line(df, x='x', y='y', title='Gráfico de línea simple')
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
