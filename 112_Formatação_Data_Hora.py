
#Formatação de data e hora
#Strftime para formatar data e hora
#Strptime para converter string em data e hora

import datetime

#Metodo strftime

data_hora = datetime.datetime(2024, 5, 7, 14, 30, 45)# Cria um objeto datetime
print(data_hora)

formato = "%d/%m/%Y %H:%M:%S" # Define o formato desejado
data_formatada = data_hora.strftime(formato) #Atribuindo o formato a variavel data_formatada
print(data_formatada)

#Metodo strptime

data_hora_str = "07/05/2024 14:30:45" # String com data e hora
formato = "%d/%m/%Y %H:%M:%S"         # Define o formato da string

data_hora = datetime.datetime.strptime(data_hora_str, formato) # Converte a string em um objeto datetime
print("Data analizada:", data_hora)