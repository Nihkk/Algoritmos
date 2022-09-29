a = float(input("Informe o coeficinte A: "))
b = float(input("Informe o coeficinte B: "))
c = float(input("Informe o coeficinte C: "))

if a == 0:
    print("\nNão é uma equação do segundo grau.")

else:
    delta = b**2 - 4*a*c 

    if delta < 0:
        print(f"Não possui raízes reais.")

    elif delta == 0:
        raízu = -b / 2*a
        print(f"A equação possui apenas uma ráiz que é: {raízu}")

    else:
        raíz1 = -b + delta**(1/2) / (2*a)
        raíz2 = -b - delta**(1/2) / (2*a)
        print(f"A equação possui duas ráizes reais que são: {raíz1} e {raíz2}")
        