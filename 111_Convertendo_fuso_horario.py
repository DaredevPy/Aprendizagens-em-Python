import pytz
import datetime


fuso_ny = pytz.timezone('America/New_York')
data_hora_ny = datetime.datetime(2024,5,7,14,30,45 , tzinfo=fuso_ny)

fuso_la = pytz.timezone('America/Los_Angeles') #fuso horario de los angeles
data_hora_la = data_hora_ny.astimezone(fuso_la) #converter a data e hora de nova york para los angeles
print(fuso_la) #imprime o fuso horario de los angeles