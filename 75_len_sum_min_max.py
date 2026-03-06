

numeros = (1,-1,1,1,2,23,3,3,4,4,4,5,5,5,5,67,600,)

print(f"Tamanho da tupla: {len(numeros)}")             #Conta o número de elementos da tupla
print(f"Menor elemento da tupla: {min(numeros)}")      #Retorna o menor elemento da tupla
print(f"Menor elemento da tupla: {max(numeros)}")      #Retorna o maior elemento da tupla
print(f"A soma dos elementos da tupla:{sum(numeros)}") ##Retorna a soma dos elementos da tupla

#tuplas poder ser feitas sem parênteses
numeros = 1,-1,1,1,2,23,3,3,4,4,4,5,5,5,5,67,600,
print(type(numeros)) #Mostra o tipo da variável