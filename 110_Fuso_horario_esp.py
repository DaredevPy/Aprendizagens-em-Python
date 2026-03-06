import pytz
import datetime



fuso_ny = pytz.timezone('America/New_York') #fuso horario de nova york
data_hora  = datetime.datetime(2024,5,7,14,30,45)
data_hora_ny = datetime.datetime(2024,5,7,14,30,45 , tzinfo=fuso_ny) #data e hora de nova york

print(data_hora)
print(data_hora_ny) #data e hora de nova york com fuso horario