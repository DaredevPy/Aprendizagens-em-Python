
arquivo = open("arquivo.txt",'a+',encoding='utf-8')
arquivo.write("Renato\n")                           #Escreve a palavra "Renato" no arquivo e \n é utilizado para pular linha
arquivo.close()
#O arquivo será aberto em modo de escrita e será adicionado a palavra "Renato" no arquivo
#a+ abre o arquivo para leitura e escrita, se o arquivo não existir, ele será criado
#encoding='utf-8' é utilizado para que o arquivo seja aberto com a codificação utf-8
palavra = "Renato"
contador = 0
#A variável contador será utilizada para contar quantas vezes a palavra "Renato" aparece no arquivo
arquivo = open("arquivo.txt",'r',encoding='utf-8',errors='replace') #errors='replace' é utilizado para substituir caracteres que não podem ser decodificados
#'r' abre o arquivo em modo de leitura
for linha in arquivo:           #Para cada linha no arquivo
    if palavra in linha:        #Se a palavra estiver na linha
        contador = contador + 1 #O contador será incrementado em 1
arquivo.close() 

print(f"A palavra {palavra} apareceu {contador} vezes no arquivo")

arquivo.close()