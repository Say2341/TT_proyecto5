import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de autos usados')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

build_histogram = st.checkbox('Construir histograma') # crear un botón
if build_histogram: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox ('Construir un grafico de dispersión') # crear un botón
if build_scatter: # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price") 
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

built_boxplot = st.checkbox ('Construir un grafico de caja') # crear un botón
if built_boxplot: # si la casilla de verificación está seleccionada
     # escribir un mensaje
    st.write('Construir un boxplot para la columna odómetro')
    
    # crear un gráfico boxplot
    fig = px.box(car_data, x='condition', y='price', color='fuel')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
