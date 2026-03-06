
animais = {
    "Rei da Selva": "Leão",
    "Maior mamifero terrestre":  "Elefante",
    "Animal que tem uma tromba": "Elefante",
    "Ave que não voa, mas é rapida correndo": "Avestruz",
    
} #Criando um dicionario com chaves e valores, onde a chave é a dica e o valor é o animal
print("Bem-vindo ao jogo'Adivinhe o animal'!")
print("Vou dar uma dica,e você tenta adivinhar o animal.")

# passo 1 - fazer o loop para jogar enquanto o usuario não acertar o animal
# passo 2 - 

for dica, resposta in animais.items(): # No dicionario animais a chave é a dica e o valor é a resposta
    while True: # loop para continuar pedindo o palpite até acertar
        try: # try para capturar erros
            palpite = input(f"Dica: {dica}. Qual animal?").strip() # Armazenando dados na variavel palpite
            if palpite.lower() == resposta.lower(): # Se o palpide for igual a reposta, independente de maiusculo ou minusculo
                print("Você acertou!")
                break # Sai do loop while e vai para a proxima dica
            else:
                print("Você errou o nome do animal!")
        except Exception as e: # Atribundindo o erro a variavel e
           print(f"Ocorreu um erro: {e}")
print("Obrigado por jogar!")           
           
        
        
        
    
    