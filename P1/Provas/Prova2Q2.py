def posição(vetor, tamanho, valor):
    for i in range(tamanho):
        if vetor[i] == valor:
            return i + 1  
         
dim = int(input("Informe o tamanho do vetor: "))

lista = [0] * dim

print(f"Digite {dim} valores: ")

for i in range(dim):
    lista[i] = int(input())

val = int(input("Qual valor você deseja encontrar: "))


print(f"O valor {val} se encontra na posição", posição(lista,dim,val),"do vetor.")