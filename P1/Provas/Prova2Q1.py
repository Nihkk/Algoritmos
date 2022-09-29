linhas = int(input(f"\nInforme o numero de linhas da matriz: "))
colunas = int(input(f"\nInforme o numero de colunas da matriz: "))
mat = []

for i in range(linhas):
    mat.append([0] * colunas)

print("")

for i in range(linhas):
    for j in range(colunas):
        mat[i][j] = int(input(f"[{i}][{j}]: "))

print("\nMatriz completa")
print("")

for i in range(linhas):
    for j in range(colunas):
        print(f"[{mat[i][j]}]", end = " ")
    print("")

print("\nMatriz transposta")
print("")

for i in range(colunas):
    for j in range(linhas):
        print(f"[{mat[j][i]}]", end = " ")
    print("")