import pandas as pd
import numpy as np
### Importando bibiotecas

### Inserindo dados em um DataFrame

df = pd.DataFrame()
print(type(df))

dados = {
    'Nome': ['João', 'Maria', 'José', 'Ana'],
    'Idade': [28, 22, 35, 30],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
    # A quantidade de dados deve ser a mesma em todas as colunas 
    # Se não for, o pandas irá gerar um erro
    #
}

df = pd.DataFrame(dados)
#print(df)

### Selecionando Culunas

Nome = df['Nome']
print(Nome)

Nome = df[['Nome','Idade']] # Imprimindo mais de uma coluna
print(Nome)