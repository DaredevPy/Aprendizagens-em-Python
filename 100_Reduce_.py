
from functools import reduce # Importando a função reduce do módulo functools
lista = [1, 2, 3, 4, 5]

reduce(lambda x, y: x + y, lista) 
# A função reduce soma todos os elementos da lista de forma acumulativa  