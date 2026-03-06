from bs4 import BeautifulSoup
import requests as req
import pandas as pd
import os
# URL do site
url = 'https://www.mat.ufmg.br/futebol/classificacao-geral_seriea/'
# Fazer a requisição ao site
resposta = req.get(url) # Atribuindo a resposta da requisição à variável 'resposta'
# Parser o conteúdo
soup = BeautifulSoup(resposta.content, 'html.parser') # Criando um objeto BeautifulSoup com o conteúdo HTML da resposta
print(soup)
tabela = soup.find('table') # Encontrando a tabela no HTML
data = [] # Lista para armazenar os dados da tabela
# Encontrar os cabeçalhos da tabela com metodos find_all()
headers = [header.text.strip() for header in tabela.find_all('th')] # List comprehension para extrair o texto dos cabeçalhos
# Pra cada linha na tabela ate a última linha
for row in tabela.find_all('tr')[1:]: 
    columns = row.find_all('td') # Encontrar todas as colunas da linha
    data.append([column.text for column in columns]) # Adicionar os dados da linha à lista 'data'
# Criar um DataFrame do Pandas com os dados 
df = pd.DataFrame(data, columns=headers) # Criando um DataFrame com os dados e os cabeçalhos
# Exibir o DataFrame
print(df)