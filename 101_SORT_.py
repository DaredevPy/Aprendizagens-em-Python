
pessoas = ['Lucas',45,'Ana',23,'João',34,'Maria',29] 
print(pessoas)
type(pessoas)

pessoas.sort(key = lambda valor: valor[1], reverse = False) # False ordena a lista de forma crescente e True de forma decrescente
print(pessoas)

#.sorte () é um método que ordena os elementos de uma lista em ordem crescente ou decrescente, dependendo do valor do parâmetro reverse. 
#valor[0] é o primeiro elemento da lista, que é o nome da pessoa.
##valor[1] é o segundo elemento da lista, que é a idade da pessoa.