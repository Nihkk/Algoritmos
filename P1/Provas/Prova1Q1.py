votaçao = 1
total_votos = 0
contador_nulos = 0
contador_brancos = 0   

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0

print("\nPara finalizar a votação digite 0 quando for requerido.")
print("\nVote 1, 2, 3 ou 4, para os candidatos respectivamente.")
print("\nVote 5 para voto nulo e 6 para voto em branco.")

while votaçao != 0:
    voto = int(input("\nQual o seu voto: "))
    
    if voto == 1:
        candidato1 = candidato1 + 1
        

    elif voto == 2:
        candidato2 = candidato2 + 1
        

    elif voto == 3:
        candidato3 = candidato3 + 1
        

    elif voto == 4:
        candidato4 = candidato4 + 1
    

    elif voto == 5:
        contador_brancos = contador_brancos + 1

    else: 
        contador_nulos = contador_nulos + 1

    total_votos = total_votos + 1

    iniciar = int(input("Votar novamente? (0 se não quiser): "))

print(f"\nO primeiro candidato teve um total de {candidato1} votos.")
print(f"O segundo candidato teve um total de {candidato2} votos.")
print(f"O terceiro candidato teve um total de {candidato3} votos.")
print(f"O quarto candidato teve um total de {candidato4} votos.")

print(f"\nO total de votos nulos foi de {contador_nulos}.")
print(f"O total de votos em branco foi de {contador_brancos}.")

porcentagem_nulos = (contador_nulos / total_votos) * 100

print(f"\nA porcentagem de votos nulos em relação ao total é de {porcentagem_nulos}%")

porcentagem_brancos = (contador_brancos / total_votos) * 100

print(f"\nA porcentagem de votos brancos em relação ao total é de {porcentagem_brancos}%")