
try:
    resultado = 10 / 0
    #resultado = 10 / 2
except Exception as e:
    print(f"Ocorreu um erro!  Tipo de erro: {e}")
else:
    print("O resultado é: {resultado}")
finally:
    print("Códigos aqui sempre serão executados")
print("Continua o programa......")
