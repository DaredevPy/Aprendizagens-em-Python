import requests
import os
api_key = "CHAVE_API_AQUI" # Substitua "CHAVE_API_AQUI" pela sua chave de API do OpenWeatherMap
cidade = "São Paulo"       # Substitua "São Paulo" pela cidade desejada
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric" 
resposta = requests.get(url) # Faz a requisição à API
dados = resposta.json() # Converte a resposta JSON em um dicionário Python
print(f"Temperatura atual da cidade {cidade}: {dados['main']['temp']}°C")
