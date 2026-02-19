#Entrada de dados

producao_mes = float (input("Entre com a quantidade de pneus prudizido: "))
garantias = float (input("Entre com a quantidade de Garantias: "))
reprocesso = float (input("Entre com a quantidade de Reprocesso: "))

#Processamento de dados

porcentagen_grt = ( garantias / producao_mes ) * 100
print (f" A porcentagen de garantias é de: {porcentagen_grt:.2f}")
porcentagen_rprc = ( reprocesso / producao_mes) * 100
print (f" A porcentagen de reprocesso é de: {porcentagen_rprc:.2f}")


#Regras de premiação

if producao_mes > 600 and producao_mes <= 1849:
    print ("Premiação de R$140,00")

if producao_mes > 1850 and producao_mes <= 1999:
    print ("Premiação de R$260,00")

if producao_mes > 2000 and producao_mes <= 2149:
    print ("Premiação de R$390,00")
    
if producao_mes > 2150 and producao_mes <= 2299:
    print ("Premiação de R$520,00")

if producao_mes >= 2300:
    print ("Premiação de R$650,00")

#Porcentagen de Garntias e Reprocesso

if porcentagen_grt > 0.70:
    print ("Meta de garantias não atingida")

if porcentagen_rprc > 0.50:
    print ("Meta de Reprocesso não atingida")