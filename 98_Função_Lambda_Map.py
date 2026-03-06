
lista = ['1', '2', '3', '4', '5']
type(lista)

lista_int =[] # Criando uma lista vazia
for numero in lista: # Para cada numero na lista
    lista_int.append(int(numero)) # Adicionando o numero convertido para inteiro na lista vazia
    
    
lista_int = list(map(int, lista)) # Fazendo a mesma coisa com map   
print(lista_int) # Imprimindo a lista de inteiros


#Função padrão que eleva ao quadrado
def quadradoNum(numero):
    return int(numero) ** 2
#resultado = quadradoNum(2)
#print(resultado) # Imprimindo o resultado da função quadradoNum

listas_quadrado = list(map(quadradoNum, lista)) # Fazendo a mesma coisa com map
print(listas_quadrado) # Imprimindo a lista de inteiros elevados ao quadrado

Lquadrado = lambda numero: int(numero) ** 2 # Criando uma função lambda que eleva ao quadrado


nova_lista2 = list(map(Lquadrado, lista)) # Fazendo a mesma coisa com map
print(nova_lista2) # Imprimindo a lista de inteiros elevados ao quadrado com lambda