def contador (maximo):
    n = 0              # Inicializa a variável n com 0, que será o contador
    while n < maximo:
        yield n        # A palavra reservada yield transforma a função em um gerador, ou seja, ela não retorna o valor de n, mas sim uma referência para o valor de n
        n+=1           # Toda vez que a função for é chamada, o valor de n é incrementado em 1
        
for numero in contador(5):
    print(numero)      # A função contador é chamada e o valor de n é impresso na tela, até que n seja igual a 5. O resultado será 0, 1, 2, 3, 4.        
    