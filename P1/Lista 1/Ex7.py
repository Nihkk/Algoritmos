salario_mensal = float(input("Informe seu salário mensal: "))
gastos_mensal = float(input("Informe seus gastos mensais: "))

economia_mensal = salario_mensal - gastos_mensal
economia_anual = economia_mensal * 12

anos_milhão = int(1000000 / economia_anual)

print(f"Nas suas condições atuais você demoraria {anos_milhão} anos para juntar 1 milhão de reais.")

