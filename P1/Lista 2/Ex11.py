num = int(input("Informe um número inteiro menor que 1000: "))

if num >= 1000:
    print(f"Informe um valor válido.")

else:
    if num >= 100:
        centena = int(num / 100)
        dezena = int((num - (centena * 100)) / 10)
        unidade = (num - ((centena * 100) + (dezena * 10)))

        if centena == 1:
            if dezena != 1 and unidade != 1: 
                print(f"{centena} centena, {dezena} dezenas e {unidade} unidades.")
            elif dezena == 1 and unidade != 1:
                print(f"{centena} centena, {dezena} dezena e {unidade} unidades.")
            elif dezena != 1 and unidade == 1:
                print(f"{centena} centena, {dezena} dezenas e {unidade} unidade.")
            else:
                print(f"{centena} centena, {dezena} dezena e {unidade} unidade.")
        
        elif dezena == 1:
            if unidade == 1:
                print(f"{centena} centenas, {dezena} dezena e {unidade} unidade.") 
            else:
                print(f"{centena} centenas, {dezena} dezena e {unidade} unidades.") 
        
        elif unidade == 1:
            print(f"{centena} centenas, {dezena} dezenas e {unidade} unidade.")

        else:
            print(f"{centena} centenas, {dezena} dezenas e {unidade} unidades.")
    
    elif num < 100 and num > 9: 
        dezena = int(num / 10)
        unidade = int((num - (dezena * 10)))

        if dezena == 1:
            if unidade == 1:
                print(f"{dezena} dezena e {unidade} unidade.") 
            else:
                print(f"{dezena} dezena e {unidade} unidades.") 
        
        elif unidade == 1:
            print(f"{dezena} dezenas e {unidade} unidade.")
        
        else:
            print(f"{dezena} dezenas e {unidade} unidades.")

    else:
        if num == 1:
            print(f"{num} unidade.")
        else: 
            print(f"{num} unidades.")
