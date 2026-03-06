#Retorna um Objeto 'filter'
#Recebe como parâmetro uma função e um objeto iterável
#Filtra a lista aplicando a função a cada elemento, retornando apenas os elementos que forem True



lista = list(range(1, 100))
print(lista)

#Cria uma outra lista
Lista_pares =[]
for elemento in lista:
    if elemento % 2 == 0:
        Lista_pares.append(elemento)
        print(Lista_pares)
        
#Aplicando o filter para resolver o mesmo problema
lista_pares2 = list(filter(lambda numero: numero % 2 == 0, lista))     
print(lista_pares2)

#Filtrando notas dos alunos
notas = [9.1,10,8.5,7.0,6.5,5.0,4.0,3.0,2.0,1.0]
print (notas)

#Obter a media das notas
from statistics import mean  #statistics é uma biblioteca padrão do Python e mean é uma função que calcula a média
media = round(mean(notas),1) #round arredonda o valor para 1 casa decimal
notas_acima_media = list(filter(lambda nota: nota >= media, notas))  #Só vai adicionar a notas_acima_media as notas que forem maiores ou iguais a media
print(f"Notas acima da media:{notas_acima_media}. A media é {media}.")

notas_abaixo_media = list(filter(lambda nota: nota <= media, notas)) #Só vai adicionar a notas_abaixo_media as notas que forem menores ou iguais a media
print(f"Notas acima da media:{notas_abaixo_media}. A media é {media}.")