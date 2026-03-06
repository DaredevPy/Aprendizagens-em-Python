
#Tratando erros com o bloco <code>try...except
#Formato
#try:
#?   'código que o python vai tentar executar'
#!except:
#?   'código que o python vai executar caso ocorra um erro no bloco try'
#!else:
#?   'código que o python vai executar caso não ocorra erro no bloco try'(opicional)
#!finally:
#?   'código que o python vai executar independente de erro ou não'(opicional)


try:
    print(10/0)
    print(nome)
except NameError: #Tratando erro de variável não definida
    print("Você não definiu a variável nome")
except ZeroDivisionError:    
    print("Você não pode dividir por zero")