nota = int(input("\nInforme uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("\nValor inválido!")
    nota = int(input("Informe um valor válido: "))

print("\nValor válido!\n")
