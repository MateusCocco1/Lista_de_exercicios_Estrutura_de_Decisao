n1=float(input("Nota 1: "))
n2=float(input("Nota 2: "))
n3=float(input("Nota 3: "))

media=(n1+n2+n3)/3

if media==10:
    print("Aprovado com distinção",media)
elif media>=7:
    print("Aprovado",media)
else:
    print("Reprovado",media)
