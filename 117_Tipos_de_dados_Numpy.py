

#Uma lista normal do Python pode conter diferentes tipos de dados, como números inteiros, strings, etc.

import numpy as np
minha_lista = [8,2,1988,"08:00", "São Paulo"]
print (type(minha_lista))
print (minha_lista)

#Uma lista Numpy só pode conter um único tipo de dado, ou seja, todos os elementos devem ser do mesmo tipo.

meu_np = np.array([8,2,1988,"08:00", "São Paulo"])
print (type(meu_np))
print (meu_np)
#Numpy pega todos os elementos da lista e transforma em string, pois é o tipo mais abrangente.

minha_lista_np = np.array([12.23, 13.34, 100, 12.23])
print (minha_lista_np)

#Numeros tipo float com numpy 