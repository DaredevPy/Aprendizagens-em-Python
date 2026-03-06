# Interators em python são objetos que permitem ser iterados, ou seja, percorridos em um loop.
# Eles são usados para representar uma sequência de dados, como listas, tuplas, dicionários, conjuntos e strings.

lista = ['Renato', 'Guilherme', 'Lucas', 'João',6,7,8,9,10] 
lista

iterator = iter(lista) # Cria um iterador a partir da lista
#next(interator) # Retorna o próximo item do iterador
#next faz como se fosse uma paginação, ou seja, ele vai passando de item em item, e quando chega no final, ele retorna um erro.
for i in iterator:
    print(i) # Imprime cada item do iterador
    
for i in iter(lista):    
    print(i) # Imprime cada item do iterador