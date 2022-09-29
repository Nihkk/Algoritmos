soma = 0
contador = 0

for i in range (1,11):
    num = int(input(f"Digite o {i}º número: "))

    soma = soma + num
    contador = contador + 1

media = soma / contador

print(f"A soma dos números é {soma} e a média é {media}.")