# O operador de desempacotamento em python é * para lista [] ou tupla ()
# ** para dicionário {}
#Ele e usado para desempacotar valores de uma coleção diretamente em variáveis

#Ex. em Collections
numeros = [1, 2, 3]
print(*numeros) #Desempacota os valores da lista e imprime 1 2 3 sem colchetes

#EX. em Strings
nome = "Renato"
print(*nome) #Desempacota os valores da string e imprime Renato sem aspas

#Ex. Desempacotamento em funções
r =range(11) #Cria um range de 0 a 10
numeros = [*r] #Desempacota os valores do range e coloca na lista numeros
print(numeros) #Imprime a lista numeros