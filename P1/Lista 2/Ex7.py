v_hora = float(input("Informe o valor da sua hora de trabalho: "))
h_mes = int(input("Informe a quantidade de horas que você trabalhou no mês: "))

salariob = v_hora * h_mes 

if salariob <= 900:
    ir = 0
    aliquota = 0

elif salariob <= 1500:
    ir = salariob * 5 / 100
    aliquota = 5

elif salariob <= 2500:
    ir = salariob * 10 / 100
    aliquota = 10

else:
    ir = salariob * 20 / 100
    aliquota = 20

sindicate = salariob * 3 / 100
fgts = salariob * 11 / 100

descontos = ir + sindicate
salariol = salariob - descontos

print(f"\nSálario Bruto: ({v_hora} + {h_mes})  : R$ {salariob}")
print(f"\n(-) IR ({aliquota}%)  : R$ {ir}")
print(f"(-) Sindicato (3%)  : R$ {sindicate}")
print(f"FGTS (11%)  : R$ {fgts}")
print(f"Total de descontos  : R$ {descontos}")
print(f"Salário Liquido  : R$ {salariol}")

