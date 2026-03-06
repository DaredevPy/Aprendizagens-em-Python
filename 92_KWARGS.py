dic_a = {
    'nome' : 'Renato',
}

dic_b = {
    'Cidade' : 'Ribeirão',
}

dic_c = {**dic_a, **dic_b} # Unindo os dicionários

print(dic_c) # Imprime o dicionário unificado


def minha_funcao(**kwargs): # Define uma função com um número variável de argumentos nomeados
    for chave, valor in kwargs.items(): # Para cada chave e valor no dicionário kwargs
        print(f'{chave} - {valor}')
        
minha_funcao(nome='Renato', idade=30, cidade='Ribeirão Preto') # Chama a função com argumentos nomeados
         