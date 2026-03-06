
#Função Padrão
def somar(x,y):
    soma = x + y
    return soma
resultado = somar(12,15)
print(resultado)

#Função Lambda
somar_2 = lambda x,y: x + y 

resultado_2 = somar_2(10,20)
print(resultado_2)

#Codigo Otimizado
somar_3 = lambda x,y: print (x + y) #Print dentro da função
somar_3(25,25)

multiplicar = lambda x,y: x * y #Multiplicação
print(multiplicar(5,5))


somar_4 = lambda *args: sum(args) #Soma de Números
print(somar_4(1,2,3,4,5,6,7,8,9,10)) #Soma de 10 números