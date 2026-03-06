
def soma (a,b,c,d,e): # Define a função soma com 5 argumentos
    return a + b + c + d + e # Soma os argumentos
print(soma(1,2,3,4,5)) # Imprime o resultado da soma dos argumentos

def soma2 (*args): # Define a função soma2 com um número variável de argumentos
    return sum(args) # Retorna a soma dos argumentos
print(soma2(1,2,3,4,5)) # Imprime o resultado da soma dos 
