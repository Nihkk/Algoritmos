num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro: "))
num3 = int(input("Digite mais um: "))

if num1 < num2 and num3 > num2:
    print(f"{num3} - {num2} - {num1}")

elif num1 < num3 and num2 > num3:
    print(f"{num2} - {num3} - {num1}")

elif num2 < num3:
    if num1 > num3:
      print(f"{num1} - {num3} - {num2}")
    else:
      print(f"{num3} - {num1} - {num2}")  

else:
    print(f"{num1} - {num2} - {num3}")