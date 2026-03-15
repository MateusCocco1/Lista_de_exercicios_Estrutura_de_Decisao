dia = int(input("Digite um número (1-7): "))

dias = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"]

if 1 <= dia <= 7:
    print(dias[dia-1])
else:
    print("Valor inválido")
