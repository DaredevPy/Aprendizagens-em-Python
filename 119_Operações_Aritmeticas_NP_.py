
lista = list(range(10))
print(lista)

print(lista + lista) #Concatenando lista
Lista2 = lista + lista
print(Lista2) #Printando lista concatenada
#listas não podem ter seus elementos multiplicados ou somados
lista3 = lista * 4
print(lista3) #Printando lista multiplicada

######### Segue abaixo o mesmo exemplo com o numpy  ######

import numpy as np
lista_np = np.array(range(50)) 
print(lista_np + lista_np)
#Para cada posição ele somou os elementos
lista_np2 = lista_np * 10 #Multiplicando os elementos por 10
print(lista_np2)
lista_np3 = lista_np **2 #Elevando os elementos ao quadrado