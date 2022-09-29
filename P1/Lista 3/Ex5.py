maior = 0

for i in range (10):
    numero = int(input("Escreva um numero: "))

    if numero > maior:
        maior = numero

print(f"\nO maior número é {maior}")