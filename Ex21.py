valor=int(input("Valor do saque: "))

for nota in [100,50,10,5,1]:
    qtd=valor//nota
    valor%=nota
    if qtd>0:
        print(qtd,"nota(s) de",nota)
