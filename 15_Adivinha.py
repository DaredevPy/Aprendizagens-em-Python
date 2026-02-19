import random 

numero_secreto = random.randint(1,100)
print("Bem vindo ao programa Adivinha")
print("Tente adivinhar o numero secreto ")

palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Digite o palpite:"))

    if palpite > numero_secreto:
        print("Palpite Acima")
    elif palpite < numero_secreto:
        print("palpite Abaixo")
    else:
        print("Parabens voce acertou o numero secreto")  