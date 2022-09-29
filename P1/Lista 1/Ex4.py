area_casa = 0

for i in range(1, 5):
    comprimento = float(input(f"Informe o comprimento do {i}º cômodo: "))
    largura = float(input(f"Informe a largura do {i}º cômodo: "))
    area_comodo = comprimento * largura 
    area_casa = area_casa + area_comodo
    print(f"A área do {i}º cômodo é igual a: {area_comodo}\n")

print(f"A área total da casa é de {area_casa} m²")    
    
