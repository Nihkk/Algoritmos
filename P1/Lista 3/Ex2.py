usuario = input("\nEscreva seu nome de usuário: ")
senha = input("Escreva sua senha: ")

while senha == usuario: 
    print("\nA SENHA NÃO PODE SER IGUAL AO SEU NOME DE USUÁRIO!")
    usuario = input("\nEscreva seu nome de usuário: ")
    senha = input("Escreva sua senha: ") 

print("\nInformações registradas!")