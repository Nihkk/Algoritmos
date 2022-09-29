valor_inicial = float(input("Informe o valor inicial da dívida: "))
atraso = int(input("Informe quantos dias de atraso tem a dívida: "))
multa = float(input("Informe o valor da multa por dia: "))

valor_final = valor_inicial + (multa * atraso)

print(f"O valor final a ser pago será de {valor_final}")

