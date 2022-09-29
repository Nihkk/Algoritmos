salario_atual = float(input("Informe o seu salário atual: "))
reajuste = float(input("Informe a porcentagem do reajuste: "))

salario_final = salario_atual + (salario_atual * (reajuste / 100)) 

print(f"Seu salário reajustado é igual a: R${salario_final}")

