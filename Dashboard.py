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
fig = px.line(dadosbacen, x='data', y='valor', labels={'tempo': 'Eixo X', 'valor': 'Eixo Y'}, title='Somatório do saldo das operações de crédito com atraso de 15 a 90 dias')

st.plotly_chart(fig)

st.header('IPCA')

urlbacenipca = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.10841/dados?formato=json&dataInicial=01/01/2010&dataFinal=31/12/2023'
response = requests.get(urlbacenipca)
dadosbacenipca = pd.DataFrame.from_dict(response.json())

# Gráfico de linhas do plotly ipca
fig_ipca = px.line(dadosbacenipca, x='data', y='valor', labels={'tempo': 'Eixo X', 'valor': 'Eixo Y'}, title='Índice de Preços ao Consumidor-Amplo (IPCA)')
st.plotly_chart(fig_ipca)


urlinflacao = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.29037/dados?formato=json&dataInicial=01/01/2010&dataFinal=31/12/2023'
response = requests.get(urlinflacao)
dadosinflacao = pd.DataFrame.from_dict(response.json())

st.header('ENDIVIDAMENTO DAS FAMÍLIAS')
fig_inflacao = px.line(dadosinflacao, x='data', y='valor', labels={'tempo': 'Eixo X', 'valor': 'Eixo Y'}, title='Endividamento das famílias em relação à renda acumulada dos últimos doze meses')
st.plotly_chart(fig_inflacao)
