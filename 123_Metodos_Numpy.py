
import numpy as np

#### arange ####

arrange_np =  np.arange(20, 50, 5) # Cria um array com valores de 20 a 50, pulando de 5 em 5
#print(arrange_np)
#print(type(arrange_np)) # Mostra o tipo do objeto

#### linspace ####

# Parametros Obrigatorios: start, stop e num opcional

# Start: numero inicial do range
# Stop: numero final do range
# Num: quantidade de elementos que queremos no range 
array_np2 = np.linspace(10,50,100) # Cria um array com 100 elementos entre 10 e 50
#print(array_np2)
#print(type(array_np2))

#### random.randint ####

## Gera um array Numpy com numeros inteiros aleatorios

#low: menor numero da distribuicao
#high: maior numero da distribuicao (opicional)
#size  Quantidade de elementos que queremos no array (opicional)

array_rand = np.random.randint(10,60,100)

#print(array_rand)

#### random.rand() ####

# Gera um array de numeros aleatorios de acordo com as dimenções especificadas.

# Parametros

array_1d = np.random.rand(10)
print(array_1d) 



