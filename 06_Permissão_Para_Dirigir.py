idade = int (input("Entre com a idade: "))
tem_cnh = int (input("CNH"))

if idade >= 18 and tem_cnh == 1:
    print ("Pode dirigir")
else:
    print ("Não pode dirigir")