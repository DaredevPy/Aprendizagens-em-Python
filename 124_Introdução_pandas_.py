import pandas as pd
import numpy as np

### Criando estruturas de dados Variadas ###

rotulos = ['a','b','c','d']
lista = list(range(100,104))
array_np = np.array(range(30,40))
dicionario = {'a':10, 'b':20, 'c':30, 'd':40}

#print( lista, array_np, dicionario, rotulos)

### Gerando Series no Pandas ###

#print (pd.Series(dicionario))

### Entendendo sobre indices e dados ###

serie = pd.Series(data=lista, index=rotulos) # Ultilizando lista como dados 'data' e rotulos como indices 'index'
print(serie)
# Se caso fornecer apenas os dados, o pandas gera automaticamente os indices
# O que eu adicionar na lista rotulos, vai ser o indice da serie

carros = pd.Series (['VOLKS','VOLKS','HYUNDAI','CHEVROLET'],index= ['GOL','FUSCA','KICKS','ONIX'])
print(carros)
print(carros['GOL']) # Acessando o valor do indice 'GOL'