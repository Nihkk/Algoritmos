valor = int(input("Quanto você quer sacar: "))

if valor > 600 or valor < 10:
    print("Este valor é inválido! Saque valores entre R$10 e R$600.")

else:
    notas100 = valor // 100
    valor = valor % 100
    notas50 = valor // 50
    valor = valor % 50
    notas10 = valor // 10
    valor = valor % 10
    notas5 = valor // 5
    notas1 = valor % 5

    print(f"Você recebe {notas100} notas de 100, {notas50} notas de 50, {notas10} notas de 10, {notas5} notas de 5, {notas1} notas de 1.")
