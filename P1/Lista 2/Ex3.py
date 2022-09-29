num1 = int(input("Digite um numero: "))
num2 = int(input("\nDigite outro numero: "))
num3 = int(input("\nDigite mais um numero: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} é o maior número.")
    else:
        print(f"{num3} é o maior número.")

elif num2 > num3:
    print(f"{num2} é o maior.")

else: 
    print(f"{num3} é o maior.")
    
