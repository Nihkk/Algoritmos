#Esse projeto foi feito pela dupla: Luan Nycholas Lemos Vieira e José Junior de Medeiros Andrade

def criar_vetores(quantidade):
    vetor = [0] * quantidade
    return vetor

def criar_filmes(vetor, quantidade):
    for i in range(quantidade):
        vetor[i] = input()

def assistidos(quantidade, vetor, nome, filmes):
    for i in range(quantidade):
        vetor[i] = input(f"{nome} você já assistiu '{filmes[i]}'? ")
        
        if vetor[i] == "s":
            vetor[i] = True
        else:
            vetor[i] = False


def recomendações(quantidade, vetor1, vetor2, filmes, contador):
    contador = 0
    for i in range(quantidade):
        if not vetor1[i] and vetor2[i]:
            print(f"{filmes[i]}")
        else:
            contador = contador + 1
        
    if contador == quantidade:
        print("Nada, você já assistiu tudo!")


quant = 10
filmes = criar_vetores(quant)
assistidos1 = criar_vetores(quant)
assistidos2 = criar_vetores(quant)
contador1 = int
contador2 = int

print(f"\nInforme os {quant} filmes a serem adicionados: ")
print("")

criar_filmes(filmes, quant)

usuario1 = input("\nInforme seu nome: ")

print("\nResponda com 's' ou 'n' para as seguintes perguntas.")
print("")

assistidos(quant, assistidos1, usuario1, filmes)

usuario2 = input("\nInforme seu nome: ")

print("\nResponda com 's' ou 'n' para as seguintes perguntas.")
print("")

assistidos(quant, assistidos2, usuario2, filmes)

print(f"\n{usuario1} nós te recomendamos: ")

recomendações(quant, assistidos1, assistidos2, filmes, contador1)

print(f"\n{usuario2} nós te recomendamos: ")

recomendações(quant, assistidos2, assistidos1, filmes, contador2)

print("")
        