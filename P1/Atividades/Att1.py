lados = int(input("Informe a quantidade de lados que o poligono possui: "))

if lados == 3:
    print("TRIÂNGULO")
    
    base = float(input("\nInforme a medida da base em cm: "))
    altura = float(input("Informe a medida da altura em cm: "))
    area_triangulo = (base * altura) / 2

    print(f"\nA área do triângulo é igual a {area_triangulo}cm²")

elif lados == 4:
    print("QUADRADO")

    lado = float(input("\nInforme a medida do lado em cm: "))
    area_quadrado = lado * lado

    print(f"\n A área do quadrado é igual a {area_quadrado}cm²")

elif lados == 5:
    print("PENTÁGONO")

elif lados < 3:
    print("Não é um polígono.")

else:
    print("Polígono não identificado.")
