import pandas as pd

#Criando uma lista de frutas
frutas = ['banana', 'maçã', 'laranja', 'uva', 'abacaxi']
#Criando um DataFrame a partir da lista de frutas
df = pd.dataframe({'frutas': frutas})
#Exibindo o DataFrame
print(df)