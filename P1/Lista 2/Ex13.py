contador = 0

print("Responda as perguntas com sim ou não (s/n): ")

p1 = input("Telefonou para a vítima? ")
if p1 == "s":
    contador = contador + 1

p2 = input("Esteve no local do crime? ")
if p2 == "s":
    contador = contador + 1

p3 = input("Mora perto da vítima? ")
if p3 == "s":
    contador = contador + 1

p4 = input("Devia para a vítima? ")
if p4 == "s":
    contador = contador + 1

p5 = input("Já trabalhou com a vítima? ")
if p5 == "s":
    contador = contador + 1

if contador == 2:
    print("Você é um suspeito.")
elif contador == 3 or contador == 4:
    print("Você é um cúmplice.")
elif contador == 5:
    print("Você é o culpado!")
else:
    print("Você é inocente.")

