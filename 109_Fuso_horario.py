
#Trabalhando com fuso horário

import pytz
#pip install pytz
fusos_horarios = pytz.all_timezones #pegar todos os fusos horarios 
print("Total de fusos horários:", len(fusos_horarios)) #total de fusos horarios
print("Alguns fuso horarios:",fusos_horarios[:10]) #pegar os 10 primeiros fusos horarios
