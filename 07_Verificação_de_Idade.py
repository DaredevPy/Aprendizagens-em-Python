#Verifica se a pessoa pode entrar na festa

idade = float (input ("Digite sua Idade:"))

if idade >= 18:
    print("Pode entrar na Festa.")
else:
    calcula = 18 - idade
    print(f"NÃO pode entrar na Festa.Você podera entrar daqui há: {calcula} anos")
print("Obrigado!")      