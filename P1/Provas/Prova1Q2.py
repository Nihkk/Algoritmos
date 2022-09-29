pessoas = 0
soma_idades = 0
executor = 1

print("\nPara finalizar o programa digite '0' quando for perguntado: ")

while executor != 0:
    idade = int(input("\nInforme sua idade: "))

    soma_idades = soma_idades + idade
    pessoas = pessoas + 1

    executor = int(input("Deseja continuar? (Digite 0 para 'não'): "))

media_idade = soma_idades / pessoas

if media_idade >= 0 and media_idade <= 25:
    print("\nA turma é classificada como JOVEM.")

elif media_idade >= 26 and media_idade <= 60:
    print("\nA turma é classificada como ADULTA.")

else:
    print("\nA turma é classificada como IDOSA.")


