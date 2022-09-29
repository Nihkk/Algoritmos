tempo = 0

massa_inicial = float(input("Informe a massa inicial em gramas: "))
massa_calculo = massa_inicial

while massa_calculo >= 0.5:

    massa_calculo = massa_calculo/2
    massa_final = massa_calculo
    tempo = tempo + 50

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = (tempo % 3600) % 60

print(f"\nA massa inicial era: {massa_inicial}")
print(f"\nA massa final é: {massa_final}")
print(f"\nA duração da reação foi de {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")