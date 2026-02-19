#Exercicio 01: Calculo de Gorjeta
conta = float (input ("Digite o valor da conta a pagar: R$ "))
percentual_gorjeta = float (input("Qual o percentual de gorjeta a ser dado: "))

#Calcular o valor da gorjeta a ser dado para o atendente
gorjeta = conta * (percentual_gorjeta / 100 ) # Atribuindo a variavel gorjeta o valor da conta multiplicado pelo percentual de gorjeta dividido por 100
total = conta + gorjeta

#Exibe o resultado
print(f"gorjeta: R$ {gorjeta: .2f} ")
print(f"Conta Total: R$ {total:.2f}")