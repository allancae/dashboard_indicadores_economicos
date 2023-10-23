import streamlit as st
import requests
import pandas as pd 
import plotly.express as px 

# st.set_page_config(layout= 'wide')

st.title('DASHBOARD - INDICADORES ECONÔMICOS :bar_chart:')

urlbacen = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21082/dados?formato=json&dataInicial=01/01/2010&dataFinal=31/12/2023'
response = requests.get(urlbacen)
dadosbacen = pd.DataFrame.from_dict(response.json())

# st.dataframe(dadosbacen)

st.header('Inadimplência BACEN')

# Gráfico de linhas do plotly 
fig = px.line(dadosbacen, x='data', y='valor', labels={'tempo': 'Eixo X', 'valor': 'Eixo Y'}, title='Gráfico de Linha a partir de um DataFrame')

st.plotly_chart(fig)

st.header('IPCA')

urlbacenipca = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.10841/dados?formato=json&dataInicial=01/01/2010&dataFinal=31/12/2023'
response = requests.get(urlbacenipca)
dadosbacenipca = pd.DataFrame.from_dict(response.json())

# Gráfico de linhas do plotly ipca
fig_ipca = px.line(dadosbacenipca, x='data', y='valor', labels={'tempo': 'Eixo X', 'valor': 'Eixo Y'}, title='Gráfico de Linha a partir de um DataFrame')
st.plotly_chart(fig_ipca)


urlinflacao = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.13522/dados?formato=json&dataInicial=01/01/2010&dataFinal=31/12/2023'
response = requests.get(urlinflacao)
dadosinflacao = pd.DataFrame.from_dict(response.json())

st.header('INFLAÇÃO')
fig_inflacao = px.line(dadosinflacao, x='data', y='valor', labels={'tempo': 'Eixo X', 'valor': 'Eixo Y'}, title='Gráfico de Linha a partir de um DataFrame')
st.plotly_chart(fig_inflacao)