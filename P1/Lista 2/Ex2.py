nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("\nInforme sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Aprovado!")

elif media >= 4 and media < 7:
    print(f"Prova final.")

else:
    print(f"Reprovado.")