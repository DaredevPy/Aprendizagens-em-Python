
times_titulos = [("Palmeiras",10),("Santos",8),("Flamengo",7),("Corinthians",7),
                 ("São paulo",6),("Cruzeiro",4),("Vasco da gama",4),("Internacional",3),("Galo",3)]
#Lista de tuplas com nomes e valores
for time ,titulos in times_titulos:
    print(f"O Time {time} possui {titulos} canecos do Brasileirão")
    
for i, (time ,titulos) in enumerate(times_titulos): #Enumerate é uma função de enumerar elementos de uma tupla 
    i+=1 #Faz com que i comece da primeira posição
    print(f"O time {time} tem {titulos} titulos. Ele é o {i}º do Brasil")