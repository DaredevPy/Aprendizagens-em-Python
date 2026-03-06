
#Exercicios: Escreva uma função em python que recebe uma lista de tuplas.
#Cada tupla tem 2 itens: nome do produto e preço.
#A Função deve retornar o nome do produto mais caro e o mais barato.
#Dica: use a função max e min para encontrar o produto mais caro e o mais barato.

#Passo 01: percorrer lista
#Passo 02: encontrar produto mais barato
#Passo 03: encontrar produto mais caro

def encontrar_produto_min_max(lista_produto): #Cria uma função que recebe uma lista de produtos
    print("")
    produto_min = produto_max = lista_produto[0] #Coloca produto_min e produto_max na primeira posição
    
    for produto in lista_produto[1:]:   # Percorre a lista de produtos começando do segundo produto
        if produto[1] < produto_min[1]: # Se o preço do produto for menor que o preço do produto_min
            produto_min = produto       # Atribui o produto atual a produto_min
            
        if produto[1] > produto_max[1]: # Se o preço do produto for maior que o preço do produto_max
            produto_max = produto       # Atribui o produto atual a produto_max
    return produto_min, produto_max     # Retorna o produto mais barato e o mais caro            
    
    
produtos = [('produto01', 10), ('produto02', 15), ('produto03', 20)] #lista de tuplas com nome do produto e preço
print(encontrar_produto_min_max(produtos))                           # Chama a função e imprime o resultado