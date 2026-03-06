#Existe uma ordem de passagem de parametros em python que deve ser seguida, conforme exemplo abaixo.
def func(posicional, *args, **kwargs):
    print("Posicional:", posicional)
    print("Args:", args)
    print("Kwargs:", kwargs)
func("posicional", 1, 2, 3, chave1="valor1", chave2="valor2")

# Função de soma que usa argumentos posicionais, *args e **kwargs:

def soma(posicional, *args, **kwargs):
    total = posicional
    total += sum(args)
    total += sum(kwargs.values())
    return total

resultado = soma(1, 2, 3, 4, chave1=5, chave2=6)
print(resultado)  # Saída: 21

