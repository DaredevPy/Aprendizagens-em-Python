salario = float (input("Salario do colaborador: "))

if salario <=1280:
    print("AUMENTO de 20%!")
    salario_reajustado = (salario * 0.20) + salario
    print(f"Seu novo salario: {salario_reajustado:}")
elif salario > 1280 and salario <=1700:
    print("AUMENTO de 15%!")
    salario_reajustado = (salario * 0.15) + salario
    print(f"Seu novo salario: {salario_reajustado:}")
elif salario > 1700 and salario <=2500:
    print("AUMENTO de 10%!")
    salario_reajustado = (salario * 0.10) + salario
    print(f"Seu novo salario: {salario_reajustado:}")
elif salario > 2500:
    print("AUMENTO de 5%!")
    salario_reajustado = (salario * 0.05) + salario  
    print(f"Seu novo salario: {salario_reajustado:}")  
