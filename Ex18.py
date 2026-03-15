data=input("Digite a data dd/mm/aaaa: ")
dia,mes,ano=map(int,data.split("/"))

if 1<=dia<=31 and 1<=mes<=12:
    print("Data válida")
else:
    print("Data inválida")
