valor_total = float (input (f"Entre com o valor da compra: "))
quantidade_itens = int (input(f"Entre com a quantidade de itens:"))
coupon_desconto = str (input (f"Entre com o codigo do coupon:"))
if valor_total >=100 and quantidade_itens >1:
    print("Parabens, você ganhou 10% de desconto comprando 2 produtos ou mais > 100 reais")
    valor_desconto = valor_total* 0.10
    valor_final = valor_total - valor_desconto
    print (f"Valor do desconto: R$ {valor_desconto:.2f}")
    print (f"Valor a Pagar: R$ {valor_final:.2f}")
elif coupon_desconto == "DESC10":
    print ("Parabens, Você ganhou 10% de desconto usando o coupon") 
    valor_desconto = valor_total * 0.10
    valor_final = valor_total - valor_desconto
    print (f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor a Pagar: R$ {valor_final:.2f}")
else:
    print(f"Sem descontos!Total da compra: R$ {valor_total:.2f}")    
