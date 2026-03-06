#Data passada e data futura com intervalo de 5 dias

import datetime

cinco_dias = datetime.timedelta(days=5) # timedelta(days=5) Subtrai 5 dias

data = datetime.date(2024, 5, 7)
data_passada = data - cinco_dias
data_futura = data + cinco_dias
print(f"Data: {data} - Data Passada: {data_passada} - Data Futura: {data_futura}") 


