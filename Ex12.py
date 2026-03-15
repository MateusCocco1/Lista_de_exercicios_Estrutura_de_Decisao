valor_hora = float(input("Valor por hora: "))
horas = float(input("Horas trabalhadas: "))

bruto = valor_hora * horas

if bruto <= 900:
    ir = 0
elif bruto <= 1500:
    ir = bruto * 0.05
elif bruto <= 2500:
    ir = bruto * 0.10
else:
    ir = bruto * 0.20

inss = bruto * 0.10
fgts = bruto * 0.11
sindicato = bruto * 0.03

descontos = ir + inss + sindicato
liquido = bruto - descontos

print("Salário bruto:", bruto)
print("IR:", ir)
print("INSS:", inss)
print("Sindicato:", sindicato)
print("FGTS:", fgts)
print("Salário líquido:", liquido)
