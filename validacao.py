from datetime import datetime, date

def ler_id(mensagem):
    valor = input(mensagem)
    while not valor.isdigit():
        print("Um ID consiste apenas em números. Tente novamente.")
        valor = input(mensagem)
    return int(valor)

def ler_id_existente(mensagem, dicionario, mensagem_erro):
    valor = ler_id(mensagem)
    while valor not in dicionario:
        print(mensagem_erro)
        valor = ler_id(mensagem)

    while not dicionario[valor]["Ativo"]:
        print(mensagem_erro)
        valor = ler_id(mensagem)
    
    return valor

def ler_id_existente_geral(mensagem, dicionario, mensagem_erro):
    valor = ler_id(mensagem)
    while valor not in dicionario:
        print(mensagem_erro)
        valor = ler_id(mensagem)
    
    return valor

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

            while len(cpf) != 11 or not cpf.isdigit():
                print("CPF inválido. Tente novamente.")
                cpf = input("Digite o CPF (apenas números): ")
        else:
            validado = True
    
    return cpf

def ler_email(mensagem, mensagem_erro):
    validado = False
    while not validado:
        email = input(mensagem)
        if email.count("@") == 1:
            email_separado = email.split("@")

            if len(email_separado) != 2 or email_separado[0].strip() == "":
                print(mensagem_erro)
                continue

            dominio = email_separado[1]
            if not "." in dominio or dominio.endswith(".") or dominio.startswith("."):
                print(mensagem_erro)
            else:
                validado = True
        else:
            print(mensagem_erro)

    return email.strip()

def ler_nome(mensagem, mensagem_erro):
    validado = False
    while not validado:
        nome = input(mensagem)
        if nome.strip() != "":
            validado = True
        else:
            print(mensagem_erro)
    return nome

def ler_data_aniversario(mensagem, mensagem_erro):
    data = input(mensagem)
    verificado = False
    
    while not verificado:
        try:
            datamodelo = datetime.strptime(data, "%d/%m/%Y").date()
            
            if datamodelo <= date.today():
                verificado = True
            else:
                print(mensagem_erro)
                data = input(mensagem)
                
        except ValueError:
            print(mensagem_erro)
            data = input(mensagem)
            
    return data
