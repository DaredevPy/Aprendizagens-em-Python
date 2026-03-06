
for i in range(10):
    if i == 5:
        print("Parando Loop")        #BREAK
        break 
    #BREAK é um comando que para o loop quando a condição é atendida.
    
for i in range(10):
    if i % 2 == 0:
            continue
    print(f"O numero {i} é impar!")  #CONTINUE
    #CONTINUE é um comando que pula a iteração atual e continua para a próxima.
    
for i in range(10):
    if i % 2 == 0:
            pass
    print(f"Valor de i: {i}.")       #PASS     
    #PASS é um comando que não faz nada, mas é necessário para o código funcionar.
     