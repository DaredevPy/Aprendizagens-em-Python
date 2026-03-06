#Metodo Deep Copy

lista1 = [1,2,3]
lista2 = lista1.copy()

print(f"lista1: {lista1}")
print(f"lista2: {lista2}")

lista1.append(10)

print(f"Lista apos inserir elementos")
print(f"lista1: {lista1}")
print(f"lista2: {lista2}")

#Cria uma lista separada

lista2.append(110)

print(f"Lista apos inserir elementos")
print(f"lista1: {lista1}")
print(f"lista2: {lista2}")

