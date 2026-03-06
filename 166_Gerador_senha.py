import string
import random
def gerar_senha(comprimento):
    carateres = string.ascii_letters + string.digits + string.punctuation  # Combina letras, números e caracteres especiais

    senha = []                                # Inicializa uma lista para armazenar os caracteres da senha
    for i in range(comprimento):              # Percorre o número de caracteres desejado
        caratere = random.choice(carateres)   # Seleciona um caractere aleatório
        senha.append(caratere)                # Adiciona o caractere à lista
    return''.join(senha)                      # Retorna a senha como uma string

senha = gerar_senha(5)
print(senha)