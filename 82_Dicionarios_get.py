#Metodos para buscar campos especificos em dicionarios

dic = {                 
    'nome' : 'Simplifica',
    'linguagem' : 'python',
    'versao' : 3.12,
    'ambiente' : 'Windows',
    'ativo' : True 
    
}

dic2 = {
    'Login' : 'Sauer',
    'Senha' : '123teste',
    
}





# print(dic.get('versao')) # Acessando o valor da chave 'versao' usando o método get()
if dic.get('linguagem'):
    print(dic.get('linguagem')) # Acessando o valor da chave 'linguagem' usando o método get()
    print(f"Linguagem: {dic['linguagem']}") # Acessando o valor da chave 'linguagem' usando a notação de colchetes
    
    dic.update(dic2) # Atualizando o dicionário com os valores do dicionário dic2 
    print(dic) # Imprimindo o dicionário atualizado