import os

# Função para limpar a tela de acordo com o sistema operacional
def limpar_tela():
    os.system('cls')#Bibloteca com funções para interagir com o sistema operacional
#Agora posso chamar esta função em qualquer lugar do código para limpar a tela


def pausa(): # Função para pausar a execução do programa
    print("\n\n") # Adiciona duas linhas em branco
    os.system('pause')# Pausa a execução do programa até que o usuário pressione uma tecla

######################################################## Funções a ser chamadas no menu principal #########################################################

# Função para mostrar o menu principal
def mostra_menu():                        #Cria uma função para mostrar o menu principal
    limpar_tela()                         #Chama a função limpar_tela para limpar a tela antes de mostrar o menu 
    print("\n\n\tSimplifica Finanças\n")  #Imprime o título do programa
    print("Menu de Opções:\n")            #Imprime o título "Menu de Opções"
    print("1 - Cadastrar Receita")        #Imprime a opção 1 para cadastrar receita
    print("2 - Cadastrar Despesa")
    print("3 - Listar Saldo")
    print("4 - Listar Extrato")
    print("5 - Sair\n")                   #Imprime a opção 5 para sair do programa

# Função para adicionar receita
def add_receita(receitas):#Cria uma função que recebe uma lista 'receitas'
    descricao = input("Digite a descrição da receita: ")          #Entrada de dados de descrição
    valor = float(input("Digite o valor da receita: "))           #Entrada de dados de valor
    receitas.append({"descricao": descricao, "valor": valor})     #Adiciona um dicionário com a descrição e o valor na lista 'receitas'
    print("Receita cadastrada com sucesso!")                      #Imprime mensagem de sucesso
    pausa()                                                       #Chama a função pausa para esperar o usuário pressionar uma tecla

# Função para adicionar despesa
def add_despesa(despesas):
    descricao = input("Digite a descrição da despesa: ")          #Entrada de dados de descrição
    valor = float(input("Digite o valor da despesa: "))           #Entrada de dados de valor
    despesas.append({"descricao": descricao, "valor": valor})     #Adiciona um dicionário com a descrição e o valor na lista 'despesas'
    print("Despesa cadastrada com sucesso!")                      #Imprime mensagem de sucesso
    pausa()                                                       #Chama a função pausa para esperar o usuário pressionar uma tecla

# Função para listar o saldo
def listar_saldo(receitas, despesas):                                  #Cria uma função que recebe duas listas 'receitas' e 'despesas'
    total_receitas = sum([receita["valor"] for receita in receitas])   #Calcula o total de receitas somando os valores da lista 'receitas'
    total_despesas = sum([despesa["valor"] for despesa in despesas])   #Calcula o total de despesas somando os valores da lista 'despesas'
    saldo = total_receitas - total_despesas                            #Calcula o saldo subtraindo o total de despesas do total de receitas
    print(f"O saldo atual é: {saldo:.2f}")                             #sum é uma função que soma os valores de uma lista
    pausa()

# Função para listar o extrato
def listar_extrato(receitas, despesas): #Cria uma função que recebe duas listas 'receitas' e 'despesas'
    print("Extrato:")  #Imprime o título "Extrato"
    print("Receitas:") #Imprime o título "Receitas"
    for receita in receitas:            #Itera sobre a lista 'receitas'
        print(f"- {receita['descricao']}: {receita['valor']:.2f}")     #Imprime a descrição e o valor da receita
    
    print("Despesas:")                                                 #Imprime o título "Despesas"
    for despesa in despesas:                                           #Itera sobre a lista 'despesas'
        print(f"- {despesa['descricao']}: {despesa['valor']:.2f}")     #Imprime a descrição e o valor da despesa
    pausa()                                                            #Chama a função pausa para esperar o usuário pressionar uma tecla

# Função principal
def main():# Cria uma função principal para organizar o fluxo do programa
    receitas = []    # Cria uma lista vazia para armazenar as receitas
    despesas = []    # Cria uma lista vazia para armazenar as despesas
    
    while True: # Inicia um loop infinito para manter o programa em execução até que o usuário decida sair
        mostra_menu() # Chama a função para mostrar o menu principal
        opcao = int(input("Escolha uma opção: ")) # Entrada de dados para escolher uma opção do menu
        
        if opcao == 1:                          # Se a opção escolhida for 1
            add_receita(receitas)               # Chama a função para adicionar receita
        elif opcao == 2:                        # Se a opção escolhida for 2
            add_despesa(despesas)               # Chama a função para adicionar despesa
        elif opcao == 3:                        # Se a opção escolhida for 3
            listar_saldo(receitas, despesas)    # Chama a função para listar o saldo
        elif opcao == 4:                        # Se a opção escolhida for 4
            listar_extrato(receitas, despesas)  # Chama a função para listar o extrato
        elif opcao == 5:                        # Se a opção escolhida for 5
            print("Saindo do programa...")      # Imprime mensagem de saída
            limpar_tela()                       # Chama a função para limpar a tela
            break                               #'break' encerra o loop e sai do programa
        else:                                   # Se a opção escolhida não for válida
            print("Opção inválida. Por favor, escolha novamente.")

# Executar o programa principal
if __name__ == "__main__": #se o arquivo for executado diretamente, chama a função main
    main()                 #Chama a função principal para iniciar o programa
