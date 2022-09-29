p1 = float(input("Informe o preço do primeiro produto: "))
p2 = float(input("\nInforme o preço do segundo produto: "))
p3 = float(input("\nInforme o preço do terceiro produto: "))

if p1 < p2:
    if p1 < p3:
        print(f"Você deve comprar o primeiro produto.")
    else:
        print(f"Você deve comprar o terceiro produto.")

elif p2 < p3:
    print(f"Você deve comprar o segundo produto.")

else: 
    print(f"Você deve comprar o terceiro produto.")