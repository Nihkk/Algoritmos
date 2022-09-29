cotação_dolar = float(input("Informe a cotação do dolar: "))
valor_real = float(input("Informe o valor em reais a ser convertido: "))

conversão = valor_real / cotação_dolar

print(f"{valor_real} reais equivale a {conversão} dólares.")