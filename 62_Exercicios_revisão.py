#Execicio_01
nome = (type("renato\n \t Pimenta")) #\n quebra de linha e \t tabulação
idade = 37
print (idade, nome)
print (type (idade)) #type diz o tipo da variavel

#Exercicios_02
nome = input("Digite seu nome:") #entrada de dados
print(f"Ola {nome}, seja bem vindo ao programa!") #Saida interativa de dados

#Exercicios_03 Operadores Aritmeticos
num_1 = float (input("Digite o primeiro numero:")) #entrada de dasdos
num_2 = float (input("Digite o segundo numero: ")) #entrada de daddos
print(f"Soma: {num_1+num_2}")
print(f"Subtr: {num_1-num_2}")
print(f"Multip: {num_1*num_2}")
print(f"Divis: {num_1/num_2}")

#Exercicios_04 Funcao que soma 2 numeros e retorna o resultado.
def soma(num_1, num_2): #Define duas variaveis 
    return num_1 + num_2 #Retorna a soma dos dois numeros

resultado = soma(5,3) #Define o valor a ser somado
print(f"Resultado da soma: {resultado}")

#Exercicios_05 Se o numero 1 for maior que o numero 2 é verdadeiro. Caso não, é falso.
num_1 = float (input("Digite o primeiro numero:")) #Entrada de dados
num_2 = float (input("Digite o segundo numero: ")) #Entrada de dados
if num_1 > num_2: #Se o primeiro numero for ">" maior que o segundo numero
    print(f"Verdadeiro")
else: #Se não
    print(f"Falso")

#Exercicios_06
idade = int ( input("Digite sua idade:"))
if idade >= 18:
    print("Você ja pode votar")
else:    #else é opcional, mas é bom usar para evitar erros.
#if idade < 18:
    print("Você ainda não pode votar")  

#Exercicios_07
frase = input("Digite uma frase: ")
print("Quantidade de caracteres:", len(frase)) #len conta a quantidade de caracteres

#Exercicios_08 Lista
numeros = []
for i in range(5):
    #num = int(input("Digite um numero:  "))
    #numeros.append(num)
    numeros.append(int(input("Digite um numero:  "))) #adiciona o numero na lista numeros
print("Lista de numeros:", numeros)  

#Exercicios_09 Dicionario
usuario = {}

usuario["nome"] = input("Digite seu nome: ")
usuario["idade"] = int(input("Digite sua idade: "))

print (f"Seu nome é : {usuario["nome"]} \n Sua idade é : {usuario["idade"]}")

#Exercicios_10 Tuplas
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

tupla = (num1, num2, num3) 

print (tupla)

#Exercicios_11 Conjunto
conj1= set(input("Digite os numeros do conj1 separados por espaço:").split())
conj2= set(input("Digite os numeros do conj2 separados por espaço:").split())

conj1.union(conj2) #união dos conjuntos 

#Exercicios_12 
num = float (input("Digite um numero: "))
if num > 0:
    print("O numero é positivo")
elif num < 0:
    print("O numero é negativo")
else:    
    print("O numero é zero")

#Exercicios_13
num = int(input("Digite um numero: "))
contador = 1

while contador <=  num:
    print(contador)
    contador = contador + 1 #contador += 1 é o mesmo que contador = contador + 1

#Exercicios_14
for i in range(1, 11):
    print(i)  

#Exercicios_15
num = int(input("Digite um numero: "))
contador = 1

while contador <=  num:
    print(contador)
    contador = contador + 1


    