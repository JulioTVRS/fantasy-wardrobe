def ler_id(mensagem):
    valor = input(mensagem)
    while not valor.isdigit():
        print("Erro: Um ID consiste apenas em números.")
        valor = input(mensagem)
    return int(valor)


def menu(titulo, opcoes):
    borda = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"

    menu = borda + "\n"
    menu += "|" + " " * 35 + "|\n"
    menu += "|" + titulo.center(35) + "|\n"
    menu += "|" + " " * 35 + "|\n"
    menu += borda + "\n"

    for opcao in opcoes:
        menu += f"| {opcao:<33} |\n"
    menu += borda

    return menu

    
    
def submenu(titulo):
    borda = "-------------------------------------"

    menu = borda + "\n"
    menu += "|" + " " * 35 + "|\n"
    menu += "|" + titulo.center(35) + "|\n"
    menu += "|" + " " * 35 + "|\n"
    menu += borda

    return menu


def ler_cpf():
    cpf = input("Digite o CPF (apenas números): ")
    while len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. Tente novamente.")
        cpf = input("Digite o CPF (apenas números): ")
        
    validado = False
    while not validado: 
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
            
        digito1 = 0
        resto1 = soma % 11
        if resto1 != 0 and resto1 != 1:
            digito1 = 11 - resto1
            
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
            
        digito2 = 0
        resto2 = soma % 11
        if resto2 != 0 and resto2 != 1:
            digito2 = 11 - resto2
            
        if digito1 != int(cpf[9]) or digito2 != int(cpf[10]) or len(set(cpf)) == 1:
            print("CPF inválido. Tente novamente.")
            cpf = input("Digite o CPF (apenas números): ")
        else:
            validado = True
    
    return cpf