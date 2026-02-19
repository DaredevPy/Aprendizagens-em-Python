#Solicitar ao Usuario os dados
valor_hora = float (input("Digite o valor da hora trabalhada:"))
horas_trabalhadas = float (input("Digite a quantidade de horas trabalhadas:"))

#Calculo do Salario Bruto
salario_bruto = valor_hora * horas_trabalhadas

print(f"Seu salario bruto é de R${salario_bruto:.2f}")

#Cauculo do IPRF

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
else:
    desconto_ir = salario_bruto * 0.20

#Calculo do INSS
desconto_inss = salario_bruto * 0.10

#Calculo do FGTS
fgts = salario_bruto * 0.11

#calculando o total de descontos
total_descontos = desconto_ir + desconto_inss + fgts

#Calculo do Salario Liquido
salario_liquido = salario_bruto - total_descontos

#Impressao em Tela 
print(f"Salario Bruto: R${salario_bruto:.2f}")
print(f"Desconto IPRF: R${desconto_ir:.2f}")
print(f"Desconto INSS: R${desconto_inss:.2f}")
print(f"Desconto FGTS: R${fgts:.2f}")
print(f"Total de Descontos: R${total_descontos:.2f}")
print(f"Salario Liquido: R${salario_liquido:.2f}")