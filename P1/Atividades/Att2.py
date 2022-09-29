individuos = 0
maior = 0

print("\nPara que o programa pare de funcionar informe -1 quando a idade for requerida.")

idade = int(input("\nInforme sua idade: "))

while idade != -1:
    sexo = input("Informe o seu sexo (masculino / feminino): ")
    olhos = input("Informe a cor dos seus olhos (azuis, verdes ou castanhos): ")
    cabelos = input("Informe a cor dos seus cabelos (louros, castanhos ou pretos: ")

    if idade > maior:
        maior = idade

    if idade >= 18 and idade <= 35 and sexo == "feminino" and olhos == "verdes" and cabelos == "louros":
        individuos = individuos + 1

    idade = int(input("\nInforme sua idade: "))

print(f"\nA maior idade da população é de {maior} anos e {individuos} são mulheres entre 18 e 35 anos que possuem olhos verdes e cabelos louros.")
        
