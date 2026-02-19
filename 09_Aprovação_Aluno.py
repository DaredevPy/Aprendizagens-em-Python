nota = float (input("Entre com o valor da nota."))
falta = float (input ("Entre com o valor de Faltas"))

if nota >70 and falta <19:
    print ("Você foi Aprovado. ")
elif nota <70 and falta <18:
    print("Reprovado por Nota. ")
elif nota >70 and falta >18:
    print ("Reprovado por Falta. ")  
elif nota <70 and falta > 18:
    print ("Reprovado por Nota e Falta")    
elif nota ==70 and falta ==18:
    print ("Passou de baixo da porta !!!")