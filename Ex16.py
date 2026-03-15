import math

a=float(input("a: "))
if a==0:
    print("Não é equação de 2º grau")
else:
    b=float(input("b: "))
    c=float(input("c: "))

    delta=b**2-4*a*c

    if delta<0:
        print("Não possui raízes reais")
    elif delta==0:
        x=-b/(2*a)
        print("Uma raiz:",x)
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print("Raízes:",x1,x2)
