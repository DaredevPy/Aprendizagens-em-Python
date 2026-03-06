
#Introdução a data e hora em python
#python tem varias bibliotecas para trabalhar com manipulação de data e hora
#Vamos fazer uso da biblioteca datetime, que é a mais comum e já vem instalada 
#Explorar seus atributos e métodos
#A biblioteca datetime tem 3 classes principais: date, time e datetime 
#A classe date tem os atributos ano, mes e dia
#A classe time tem os atributos hora, minuto, segundo e microsegundo


#Importando a biblioteca datetime
import datetime
#Criar data especifica
data = datetime.date(2023, 10, 6)
print(f"Data:{data.year}")  #Atributo ano
print(f"Data:{data.month}") #Atributo mes
print(f"Data:{data.day}")   #Atributo dia

#Criar hora especifica
tempo = datetime.time(13, 30, 45)
print(f"Hora:{tempo.hour}")  #Atributo hora
print(f"Hora:{tempo.minute}") #Atributo minuto
print(f"Hora:{tempo.second}")  #Atributo segundo

#Criar data e hora usando variáveis
minuto = tempo.minute
segundo = tempo.second
hora = tempo.hour
print(f"Hora:{hora}:{minuto}:{segundo}") 

#Criar data e hora usando variáveis 2
data_hora = datetime.datetime(2023, 10, 6, 13, 30, 45)
ano = data_hora.year
mes = data_hora.month
dia = data_hora.day
hora = data_hora.hour
minuto = data_hora.minute
segundo = data_hora.second
print(f"Data e Hora:{ano}-{mes}-{dia} {hora}:{minuto}:{segundo}")

#Criando uma variavel da hora atual
agora = datetime.datetime.now()
print(agora) #Hora atual

hoje = datetime.date.today()
print(hoje) #Data atual
