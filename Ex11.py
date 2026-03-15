salario = float(input("Digite o salário: "))

if salario <= 280:
    aumento = 0.20
elif salario <= 700:
    aumento = 0.15
elif salario <= 1500:
    aumento = 0.10
else:
    aumento = 0.05

valor = salario * aumento
novo = salario + valor

print("Salário antes:", salario)
print("Percentual:", aumento*100,"%")
print("Aumento:", valor)
print("Novo salário:", novo)
