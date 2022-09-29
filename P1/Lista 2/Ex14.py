tipo = input("Qual tipo de combustível você quer? Gasolina(g) ou Álcool(a): ")
if tipo != "g" and tipo != "a":
    print("Escolha um tipo disponível. Gasolina(g) ou Álcool(a).")

else:
 litro = int(input("Informe quantos litros você quer abastecer: "))

 if tipo == "g":
    preço = 4.50 * litro

    if litro <= 20:
        porc = 4 * litro
        desconto = preço * (porc / 100)
        preço_final = (preço - desconto)

        print(f"O valor a ser pago é de R${preço_final}")

    else:
        porc = 6 * litro
        desconto = preço * (porc / 100)
        preço_final = (preço - desconto)

        print(f"O valor a ser pago é de R${preço_final}")

 else:
    preço = 3.40 * litro

    if litro <= 20:
        porc = 3 * litro
        desconto = preço * (porc / 100)
        preço_final = (preço - desconto)

        print(f"O valor a ser pago é de R${preço_final}")

    else:
        porc = 5 * litro
        desconto = preço * (porc / 100)
        preço_final = (preço - desconto)

        print(f"O valor a ser pago é de R${preço_final}")





