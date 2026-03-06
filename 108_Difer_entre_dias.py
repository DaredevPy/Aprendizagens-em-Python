import datetime
#Diferença entre duas datas
data = datetime.date(2024, 5, 7)
data2 = datetime.date(2023, 1, 1)
diferenca = data - data2

print(f"Diferença em dias:" ,diferenca.days) #Imprimindo a diferença em dias
print(f"Diferença em semanas:" ,diferenca.days/7) #Imprimindo a diferença em semanas