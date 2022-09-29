km_inicial = int(input("Informe a quilometragem inicial: "))
km_final = int(input("Informe a quilometragem final: "))
litros = int(input("Informe a quantidade de litros gastos no percurso: "))

distância = km_final - km_inicial

media_consumo = distância / litros

print (f"A média de consumo do véiculo é de {media_consumo} km/l")