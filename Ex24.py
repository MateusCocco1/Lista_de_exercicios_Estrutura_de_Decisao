a=float(input("Número 1: "))
b=float(input("Número 2: "))

op=input("Operação (+ - * /): ")

if op=="+":
    r=a+b
elif op=="-":
    r=a-b
elif op=="*":
    r=a*b
else:
    r=a/b

print("Resultado:",r)

if r%2==0:
    print("Par")
else:
    print("Ímpar")

if r>=0:
    print("Positivo")
else:
    print("Negativo")

if r==int(r):
    print("Inteiro")
else:
    print("Decimal")
