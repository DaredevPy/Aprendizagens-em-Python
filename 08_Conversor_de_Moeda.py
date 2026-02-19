#Conversor de Real para Dolar
valor_real = float ( input("Digite o Valor em Real: R$ "))
taxa_cambio = 1/5

#calcular o valor em Dolar 
valor_dolar = valor_real * taxa_cambio

#Exibir o resultado
print (f"O Valor de R${valor_real} vale ${valor_dolar}")