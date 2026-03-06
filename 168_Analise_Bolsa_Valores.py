import yfinance as yf
import matplotlib.pyplot as plt

# Lista de simbolos das ações
acoes = ['ITSA4.SA', 'PETR3.SA', 'VALE3.SA', 'BBDC.SA', 'ABEV3.SA'] # Coloque aqui os códigos das ações que deseja analisar

# Obter os daddos historicos para cada ação 
dados_acoes = {}                                                                # Dicionário para armazenar os dados das ações
for acao in acoes:                                                              # Loop através de cada ação na lista
    dados_acoes[acao] = yf.download(acao, start='2022-01-01', end='2022-12-31') # Baixar os dados históricos de cada ação entre as datas especificadas
    
#Gerar os gráficos    
plt.figure(figsize=(12, 8 ))                                                    # Definir o tamanho da figura do gráfico
for acao, dados in dados_acoes.items():                                         # Loop através de cada ação e seus dados
    plt.plot(dados.index, dados['Close'], label=acao)                           # Plotar o preço de fechamento da ação ao longo do tempo
plt.title('Histórico de Preços das Ações')                                      # Título do gráfico
plt.xlabel('Data')                                                              # Rótulo do eixo x
plt.ylabel('Preço de Fechamento (R$)')                                          # Rótulo do eixo y
plt.legend()                                                                    # Adicionar legenda para identificar as ações
plt.grid(True)                                                                  # Adicionar grade ao gráfico
plt.show()                                                                      # Exibir o gráfico

# yfinance é uma biblioteca que permite acessar dados financeiros do Yahoo Finance.
# matplotlib é uma biblioteca de plotagem que permite criar gráficos em Python.
# A lista de ações contém os códigos das ações que serão analisadas.   