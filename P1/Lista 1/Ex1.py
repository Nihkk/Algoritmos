valor_litro = float (input("Informe o valor do litro do combustível: "))
valor_pago = float (input("Informe quanto você quer reabastecer em reais: "))

litros = valor_pago / valor_litro

print (f'Você reabasteceu {litros} litros de gasolina.')