pontos=0

for p in range(5):
    r=input("Responda s/n: ")
    if r=="s":
        pontos+=1

if pontos==2:
    print("Suspeita")
elif 3<=pontos<=4:
    print("Cúmplice")
elif pontos==5:
    print("Assassino")
else:
    print("Inocente")
