num1 = int(input("Escolha o primeiro número: "))
num2 = int(input("Escolha o segundo número: "))

if num1 > num2:
    for i in range(num2+1,num1):
        print(i, end=" ")

else: 
    for i in range(num1+1,num2):
        print(i, end=" ")

