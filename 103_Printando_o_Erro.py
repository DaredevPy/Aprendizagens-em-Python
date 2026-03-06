
try:
    print(10 / 0)
except Exception as e:   #Exception é a classe pai de todas as exceções de Python
    print(f"Erro: {e}")  # imprime o erro e o tipo de erro '{e}'   