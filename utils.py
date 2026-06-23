def ler_id(mensagem):
    valor = input(mensagem)
    while not valor.isdigit():
        print("Erro: Um ID consiste apenas em números.")
        valor = input(mensagem)
    return int(valor)


def ler_cpf():
    cpf = input("Digite o CPF (apenas números): ")
    while len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. Tente novamente.")
        cpf = input("Digite o CPF (apenas números): ")
    return cpf