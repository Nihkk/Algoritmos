comprimento_sala = float (input('Qual o comprimento da sala: '))
largura_sala = float (input('Qual a largura da sala: '))

comprimento_cadeira = float (input('Qual o comprimento da cadeira: '))
largura_cadeira = float (input('Qual a largura da cadeira: '))

cadeiras_largura = (largura_sala + 0.5) // (largura_cadeira + 0.5)
cadeiras_comprimento = (comprimento_sala - 1.5 + 0.2) // (comprimento_cadeira + 0.2)

cadeiras = cadeiras_largura * cadeiras_comprimento

print(f"Cabem {cadeiras} cadeiras na sala.")