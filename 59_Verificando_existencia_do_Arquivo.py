
import os 
#importando bilbioteca os

if os.path.exists("arquivo.txt"):
    arquivo = open("arquivo.txt","r")
    print("Arquivo encontrado")
    #se o arquivo existir, ele será aberto em modo de leitura
else:
    print("Arquivo não encontrado")
    #se o arquivo não existir, será exibida a mensagem "Arquivo não encontrado"