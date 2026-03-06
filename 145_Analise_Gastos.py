import streamlit as st
import pandas as pd
import plotly.express as px

      
      ### Logica do programa  ###

# Carregar os dados /p pandas (dataframe)
def carregar_dados(caminho_arquivo):    # Função para carregar os dados
      df = pd.read_csv(caminho_arquivo) # Lê o arquivo CSV e armazena em um DataFrame 
      return df



# Preparar os dados
def preparar_dados(df):
    df.dropna(inplace=True)                                                 # Remove linhas com valores ausentes
    df['data_compra'] = pd.to_datetime(df['data_compra'],format='%d/%m/%Y') # Converte a coluna de data para o tipo datetime
    df['valor'] = df['valor'].astype(float)                                 # Converte a coluna de valor para o tipo float
    df['mes'] = df['data_compra'].dt.to_period('M').astype(str)             # Extrai o mês da data de compra e converte para string
    return df
# astype converte o tipo de dado para string
# dt.to_period('M') converte a data para o período mensal


# Calcular gastos por mês de cada cartão
def calcular_total_gastos_mensais(df):
    total_gastos_mensais = df.groupby(['mes','nome'])['valor'].sum().unstack()
    return total_gastos_mensais
# Agrupando colunas 'mes' , 'nome' e somando os valores da coluna 'valor'
# ustack() transforma o dataframe em uma série com multi-índice



# Mostrar categorias de gastos mais frequentes
def identificar_categorias_frequentes(df):                               
    categorias_frequentes = df['categoria'].value_counts().reset_index()   # Conta a frequência de cada categoria e reseta o índice
    categorias_frequentes.columns = ['Categoria', 'Frequencia']            # Renomeia as colunas do DataFrame resultante
    return categorias_frequentes  



# Carregar dados
caminho_arquivo = 'cartoes.csv'
df = carregar_dados(caminho_arquivo)

# Preparar os dados
df = preparar_dados(df)

# Calcular total de gatos por mês de cada cartão
total_gastos_mensais = calcular_total_gastos_mensais(df)


print(identificar_categorias_frequentes(df))

### Publica os graficos e tabelas ###


st.title('Análise de Gastos com Cartões de Crédito')   # Título da página
st.header('Grafico de Gastos por Mês em cada Usuario') # Subtítulo da página
fig_gastos_mensais = px.line(total_gastos_mensais,
                             x=total_gastos_mensais.index,
                             y=total_gastos_mensais.columns,
                             labels={'value': 'Total de Gastos', 'mes': 'Mês'},
                             title='Total de Gastos Mensais por Usuário')  # Cria um gráfico de linha com os dados de gastos mensais
st.plotly_chart(fig_gastos_mensais)  # Exibe o gráfico de gastos mensais


st.header('Frequência de Categorias de Gastos')  # Subtítulo da página
categorias_frequentes = identificar_categorias_frequentes(df)
fig_categorias_frequencia = px.bar(categorias_frequentes,
                                   x='Categoria',
                                   y='Frequencia',
                                   labels={'Categoria': 'Categoria', 'Frequencia': 'Frequência'},
                                   title='Frequência de Categorias de Gastos')  # Cria um gráfico de barras com as categorias de gastos
st.plotly_chart(fig_categorias_frequencia)  # Exibe o gráfico de frequência de categorias de gastos

### Exibir os dados em tabela ###

st.header("Dados Processados:")  # Subtítulo para a tabela de dados
st.subheader("Gastos Por Pessoa")  # Subtítulo para a tabela de gastos por pessoa
st.dataframe(total_gastos_mensais)  # Exibe a tabela de gastos mensais por usuário


st.subheader('Categoria de frequência de Gastos:')
st.dataframe(categorias_frequentes,width=700)









### codigo usado no terminal para conectar com navegador ###
# C:\Users\Python\AppData\Local\Programs\Python\Python313\Scripts\streamlit.exe run .\145_Analise_Gastos.py

# Exibir os dados no navegador