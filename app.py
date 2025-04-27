import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título principal
st.title('Panel Interactivo de Ventas')

# Subida de archivo
archivo_csv = st.file_uploader("Sube tu archivo CSV", type=["csv"])

# Condición: Si se sube un archivo
if archivo_csv:
    # Leer archivo
    datos = pd.read_csv(archivo_csv)

    # Mostrar el dataframe
    st.subheader('Vista previa de los datos')
    st.dataframe(datos)

    # Selección de una columna para graficar
    columna = st.selectbox('Selecciona una columna para analizar:', datos.columns)

    # Gráfico de distribución
    st.subheader(f'Distribución de valores en {columna}')
    fig, ax = plt.subplots()
    datos[columna].hist(bins=20, ax=ax, color='skyblue', edgecolor='black')
    plt.xlabel(columna)
    plt.ylabel('Frecuencia')
    plt.grid(True)
    st.pyplot(fig)
