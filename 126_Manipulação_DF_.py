import pandas as pd
import numpy as np
### Importando bibiotecas
    ### Manipulação Básica de DataFrames ###
dados = {
    'Nome': ['João', 'Maria', 'José', 'Ana'],
    'Idade': [28, 22, 35, 30],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
    # A quantidade de dados deve ser a mesma em todas as colunas 
    # Se não for, o pandas irá gerar um erro
    }
df = pd.DataFrame(dados)
#print(df)
## Adicionando uma nova coluna com base em outra coluna
df['Idade_nova'] = df['Idade'] + 5 # Usando operações aritméticas
#print("\n \n \n",df) 

    ### Operaçãoes em Dataframe ###
    
nome = df['Nome'] # Imprimindo coluna especifica    
print(nome)

df['Idade_nova'] * 2 # Multiplicando a nova coluna por 2
df['Idade_nova'] = df['Idade_nova'] * 2 # Atualizando a coluna com o novo valor 

## Apagando colunas

del df['Idade_nova'] # Deletando a coluna criada


df.drop('Idade', axis=1) # Deletando a coluna Idade
#print("\n \n \n",df)