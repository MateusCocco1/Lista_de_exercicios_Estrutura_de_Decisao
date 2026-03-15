n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1+n2)/2

if media >= 9:
    conceito="A"
elif media >= 7.5:
    conceito="B"
elif media >= 6:
    conceito="C"
elif media >= 4:
    conceito="D"
else:
    conceito="E"

print("Média:", media)
print("Conceito:", conceito)

if conceito in ["A","B","C"]:
    print("APROVADO")
else:
    print("REPROVADO")
