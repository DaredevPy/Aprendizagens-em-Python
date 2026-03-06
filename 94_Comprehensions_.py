

#Comprehensions

# - Forma mais concisa de gerar coleções em apenas uma linha de codigo
# - Podem conter testes logicos
# - Podem usar expreções Lambdas

#Aplicações:
# - Maior facilidade de escrever codigo
# - Podem substituir loops, 'map()' e 'filter()' em muitas situações
# - Podem ser muito performaticos

# Ex_01 Codigo escrito de forma normal
quadrado = []
for x in range(10):
    quadrado.append(x**2)                                                                                  #Levar ao cubo**3
print(quadrado)   

# Codigo escrito com metodo Comprehensions
quadrado=[x**2 for x in range(10)]
print(quadrado)

#Ex_02 - Lista de pares 
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
print(pares)        

# Codigo escrito com metodo Comprehensions

pares = [i for i in numeros if i % 2 == 0]
print(pares)

#Ex_03 - Lista de strings

palavras = ['python', 'java', 'c++', 'javascript', 'ruby']
for palavra in palavras:
    print(palavra.upper())
    
# Codigo escrito com metodo Comprehensions   
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas) 