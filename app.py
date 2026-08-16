# importing the necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# reading the data file
car_data = pd.read_csv('vehicles.csv') 

# creating a button to create a histogram
hist_button = st.button('Criar histograma') 

# if the button is clicked
if hist_button: 
    # writing a message to the user
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # crating a histogram using Plotly Express
    fig = px.histogram(car_data, x="odometer")

    # showing a Plotly interactive chart
    st.plotly_chart(fig, use_container_width=True)

# creating a button to create a scatter plot
scatter_button = st.button('Create scatter plot')

# if the button is clicked
if scatter_button:
    # writing a message to the user
    st.write('Creating a scatter plot for the car sales listings dataset')

    #showing a scatter plot using Plotly Express
    fig2 = px.scatter(car_data, x='odometer', y='prices')

    # showing a Plotly interactive chart
    st.plotly_chart(fig2, use_container_width=True)
    