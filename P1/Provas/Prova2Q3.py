def maior_matriz(matriz, linhas, colunas):
    maior = 0
    lista = [0] * 3

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                lista[0] = maior
                lista[1] = i + 1
                lista[2] = j + 1
    return lista

lin = int(input("\nInforme o numero de linhas da matriz: "))
col = int(input("\nInforme o numeroo de colunas da matriz: "))

matrix = []

for i in range(lin):
    matrix.append([0] * col)

print("")

for i in range(lin):
    for j in range(col):
        matrix[i][j] = int(input(f"[{i+1}][{j+1}]: "))

print("")

resultado = maior_matriz(matrix, lin, col)

print(f"O maior valor é o número {resultado[0]} que se encontra na linha {resultado[1]}, coluna {resultado[2]} da matriz.")

