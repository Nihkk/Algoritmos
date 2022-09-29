morangos = int(input("Quantos quilos de morango você quer: "))
if morangos <= 5:
    preço1 = 2.50 * morangos
else:
    preço1 = 2.20 * morangos

maçãs = int(input("Quantos quilos de maçã você quer: "))
if maçãs <= 5:
    preço2 = 1.80 * maçãs
else:
    preço2 = 1.50 * maçãs

total_quilos = morangos + maçãs
preço_total = preço1 + preço2

if total_quilos > 8 or preço_total > 25:
    desconto = preço_total * (10 / 100)
    preço_total = preço_total - desconto

    print(f"O total a ser pago é de R${preço_total}")

else:
    print(f"O total a ser pago é de R${preço_total}")