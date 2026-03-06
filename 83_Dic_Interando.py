# dic.values()
# dic.items()
# dic.keys()



dic = {                 
    'nome' : 'Simplifica',
    'linguagem' : 'python',
    'versao' : 3.12,
    'ambiente' : 'Windows',
    'ativo' : True 
    
}

for chave in dic.keys():
    print(chave)         # Imprimindo as chaves do dicionário usando o método keys()
    print(chave, dic[chave]) # Imprimindo as chaves e seus respectivos valores usando a notação de colchetes
    
for valor in dic.values(): # Iterando sobre os valores do dicionário
    print(valor)    # Imprimindo os valores do dicionário usando o método values()
    
for chave, valor in dic.items(): # Iterando sobre os pares chave-valor do dicionário
    print(chave, valor) # Imprimindo as chaves e seus respectivos valores usando o método items()    
    