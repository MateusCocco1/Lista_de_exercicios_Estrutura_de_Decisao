tipo=input("Tipo (F,A,P): ")
kg=float(input("Quantidade kg: "))
cartao=input("Cartão Tabajara (s/n): ")

if tipo=="F":
    preco=4.9 if kg<=5 else 5.8
elif tipo=="A":
    preco=5.9 if kg<=5 else 6.8
else:
    preco=6.9 if kg<=5 else 7.8

total=kg*preco

desconto=0
if cartao=="s":
    desconto=total*0.05

final=total-desconto

print("Total:",total)
print("Desconto:",desconto)
print("Valor a pagar:",final)
