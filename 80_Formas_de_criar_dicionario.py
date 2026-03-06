#Formas de criar dicionario

dic = {}        # Forma 1: Usando chaves
print(type(dic))

dic_2 = {'marca': 'Fiat', # Forma 2: Usando chaves e valores
       'modelo': 'Pulse'
       }
print(dic_2)

dados = dict()
print(type(dados))        # Forma 3: Usando a função dict()

dados = dict(marca='Fiat', modelo='Pulse') # Forma 4: Usando a função dict() com argumentos nomeados

