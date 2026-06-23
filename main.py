import os
import pickle


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


def ler_valor():
    while True:
        try:
            valor = float(input("Digite o valor do produto: "))
        except ValueError:
            print("Erro: Digite um número válido.")
            continue

        if valor < 0:
            print("Erro: O valor do produto não pode ser negativo.")
            continue

        return valor


def ler_tamanho():
    print("Padrão de tamanhos: (PP, P, M, G, GG, XG)")
    tamanho = input("Digite o tamanho do produto: ")
    while tamanho.lower() not in ["pp", "p", "m", "g", "gg", "xg"]:
        print("Tamanho inválido. Tente novamente! Tamanhos válidos: (PP, P, M, G, GG, XG)")
        tamanho = input("Digite o tamanho do produto: ")
    return tamanho.upper()


def ler_categoria():
    print("Categorias válidas: Comum (1), Fantasia (2)")
    categoria = input("Digite o número da categoria do produto: ")
    while categoria != "1" and categoria != "2":
        print("Categoria inválida. Tente novamente! Categorias válidas: Comum (1), Fantasia (2)")
        categoria = input("Digite o número da categoria do produto: ")
    return "Comum" if categoria == "1" else "Fantasia"


def ler_id_existente(mensagem, dicionario, mensagem_erro):
    valor = ler_id(mensagem)
    while valor not in dicionario:
        print(mensagem_erro)
        valor = ler_id(mensagem)
    return valor


# Dicionários já com dados para acelerar os testes

roupas = {              
    1: {
        "Nome": "Terno",
        "Valor": 80,
        "Descricao": "Terno preto com gravata.",
        "Tamanho": "G",
        "Categoria": "Comum",
        "Ativo": True
    }
}

clientes = {
    1: {
        "Nome": "Fulano de Tal",
        "CPF": "12345678900",
        "Telefone": "(84) 12345-6789",
        "Email": "fulano5@gmail.com",
        "Endereco": "Rua das Palmeiras, 245, Lagoa Nova, Natal - RN, CEP 59075-320",
        "Ativo": True
    }
}

funcionarios = {
    1: {
        "Nome": "Beltrano da Silva",
        "CPF": "98765432100",
        "Telefone": "(84) 54321-6789",
        "Email": "beltrano1@gmail.com",
        "Endereco": "Rua das Palmeiras, 246, Lagoa Nova, Natal - RN, CEP 59075-320",
        "Ativo": True
    }
}

locacoes = {
    1: {
        "ID_Cliente": 1,
        "ID_Produto": 1,
        "CheckIn": "25/05/2026",
        "CheckOut": "30/06/2026",
        "Ativo": True
    }
}



try:
    roupasArquivo = open("roupas.dat", "rb")
    roupas = pickle.load(roupasArquivo)
    roupasArquivo.close()
except:
    roupasArquivo = open("roupas.dat", "wb")
    roupasArquivo.close()
    
try:
    clientesArquivo = open("clientes.dat", "rb")
    clientes = pickle.load(clientesArquivo)
    clientesArquivo.close()
except:
    clientesArquivo = open("clientes.dat", "wb")
    clientesArquivo.close()

try:
    funcionariosArquivo = open("funcionarios.dat", "rb")
    funcionarios = pickle.load(funcionariosArquivo)
    funcionariosArquivo.close()
except:
    funcionariosArquivo = open("funcionarios.dat", "wb")
    funcionariosArquivo.close()
    
try:
    locacoesArquivo = open("locacoes.dat", "rb")
    locacoes = pickle.load(locacoesArquivo)
    locacoesArquivo.close()
except:
    locacoesArquivo = open("locacoes.dat", "wb")
    locacoesArquivo.close()

resp = ""
while resp != "0":
    os.system("cls" if os.name == "nt" else "clear")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("|-                                 -|")
    print("|-         Fantasy Wardrobe        -|")
    print("|-                                 -|")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("|-   1 - Roupas e Fantasias        -|")
    print("|-   2 - Clientes                  -|")
    print("|-   3 - Funcionários              -|")
    print("|-   4 - Gerenciar Locação         -|")
    print("|-   5 - Relatórios                -|")
    print("|-   6 - Sobre o Sistema           -|")
    print("|-   0 - Sair                      -|")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    resp = input("Digite o número do módulo que quer acessar: ")

    if resp == "1":

        resp_roupas = ""
        while resp_roupas != "0":
            os.system("cls" if os.name == "nt" else "clear")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-                               -|")
            print("|-        Módulo de Roupas       -|")
            print("|-          e Fantasias          -|")
            print("|-                               -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-  1 - Listar produto           -|")
            print("|-  2 - Adicionar produto        -|")
            print("|-  3 - Remover produto          -|")
            print("|-  4 - Atualizar produto        -|")
            print("|-  0 - Voltar                   -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            resp_roupas = input("Digite o número do submódulo que quer acessar: ")

            if resp_roupas == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-      Visualizar produto       -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()
                
                if len(roupas) > 0:
                    id_produto = ""
                    while id_produto != 0:
                        id_produto = ler_id("Digite o ID do produto (ou 0 para cancelar): ")

                        if id_produto != 0:
                            if id_produto in roupas:
                                if roupas[id_produto]["Ativo"]:
                                    print()
                                    print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                                    print("Descrição:", roupas[id_produto]["Descricao"])
                                    print()
                                else:
                                    print()
                                    print(f"Produto com ID ({id_produto}) inativo. (Excluído)")
                                    print()
                            else:
                                print()
                                print(f"Produto com ID ({id_produto}) não encontrado.")
                                print()
                else:
                    print("Não existe nenhum produto cadastrado no sistema.")

                print()
                input("Aperte (ENTER) para continuar.")
                print()

            elif resp_roupas == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-        Adicionar produto      -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                nome_produto = input("Digite o nome do produto: ")
                valor_produto = ler_valor()
                desc_produto = input("Digite a descrição do produto: ")
                tam_produto = ler_tamanho()
                ctg_produto = ler_categoria()

                id_produto = 1
                if len(roupas) > 0:
                    id_produto = list(roupas.keys())[-1] + 1

                roupas[id_produto] = {
                    "Nome": nome_produto.capitalize(),
                    "Valor": valor_produto,
                    "Descricao": desc_produto,
                    "Tamanho": tam_produto,
                    "Categoria": ctg_produto,
                    "Ativo": True
                }

                print("(ID: %d) Produto adicionado com sucesso!" % id_produto)
                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_roupas == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-        Remover produto        -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_produto = ""
                encontrado = False
                while not encontrado:
                    id_produto = ler_id("Digite o ID do produto (ou 0 para cancelar): ")

                    if id_produto == 0:
                        encontrado = True
                        continue

                    if id_produto in roupas:
                        encontrado = True
                        print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                        print("Descrição:", roupas[id_produto]["Descricao"])
                        print("Tem certeza que deseja remover esse produto?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                        if decisao.lower() == "s":
                            roupas[id_produto]["Ativo"] = False
                            print("Produto removido com sucesso!")
                    else:
                        print("Não existe um produto com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_roupas == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-        Atualizar produto      -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_produto = ""
                encontrado = False
                while not encontrado:
                    id_produto = ler_id("Digite o ID do produto (ou 0 para cancelar): ")

                    if id_produto == 0:
                        encontrado = True
                        continue

                    if id_produto in roupas:
                        if roupas[id_produto]["Ativo"]:
                            encontrado = True
                            print("Informações antigas:")
                            print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                            print("Descrição:", roupas[id_produto]["Descricao"])

                            print()
                            print("Informações novas:")
                            nome_produto = input("Digite o nome do produto: ")
                            valor_produto = ler_valor()
                            desc_produto = input("Digite a descrição do produto: ")
                            tam_produto = ler_tamanho()
                            ctg_produto = ler_categoria()

                            roupas[id_produto] = {
                                "Nome": nome_produto.capitalize(),
                                "Valor": valor_produto,
                                "Descricao": desc_produto,
                                "Tamanho": tam_produto,
                                "Categoria": ctg_produto,
                                "Ativo": True
                            }

                            print("Produto atualizado com sucesso!")
                            
                            print()
                            print("Informações novas:")
                            print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                            print("Descrição:", roupas[id_produto]["Descricao"])
                        else:
                            print("Produto inativo. (Removido)")
                    else:
                        print("Não existe um produto com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

    elif resp == "2":

        resp_clientes = ""
        while resp_clientes != "0":
            os.system("cls" if os.name == "nt" else "clear")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-                               -|")
            print("|-       Módulo de Clientes      -|")
            print("|-                               -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-  1 - Listar clientes          -|")
            print("|-  2 - Adicionar cliente        -|")
            print("|-  3 - Remover cliente          -|")
            print("|-  4 - Atualizar cliente        -|")
            print("|-  0 - Voltar                   -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            resp_clientes = input("Digite o número do submódulo que quer acessar: ")

            if resp_clientes == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-      Visualizar cliente        -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                if len(clientes) > 0:
                    id_cliente = ""
                    while id_cliente != 0:
                        id_cliente = ler_id("Digite o ID do cliente (ou 0 para cancelar): ")

                        if id_cliente != 0:
                            if id_cliente in clientes:
                                if clientes[id_cliente]["Ativo"]:
                                    print()
                                    print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                                    print("Endereço:", clientes[id_cliente]["Endereco"])
                                    print()
                                else:
                                    print()
                                    print(f"Cliente com ID ({id_cliente}) inativo. (Excluído)")
                                    print()
                            else:
                                print()
                                print(f"Cliente com ID ({id_cliente}) não encontrado.")
                                print()
                else:
                    print("Não existe nenhum cliente cadastrado no sistema.")

                print()
                input("Aperte (ENTER) para continuar.")
                print()

            elif resp_clientes == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-       Adicionar cliente       -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                nome_cliente = input("Digite o nome do cliente: ")
                cpf_cliente = ler_cpf()

                print("Modelo de telefone: (00) 00000-0000")
                tel_cliente = input("Digite o telefone do cliente: ")

                email_cliente = input("Digite o e-mail do cliente: ")

                endereco_cliente = input("Digite o endereço do cliente: ")

                id_cliente = 1
                if len(clientes) > 0:
                    id_cliente = list(clientes.keys())[-1] + 1

                clientes[id_cliente] = {
                    "Nome": nome_cliente.title(),
                    "CPF": cpf_cliente,
                    "Telefone": tel_cliente,
                    "Email": email_cliente,
                    "Endereco": endereco_cliente,
                    "Ativo": True
                }

                print("(ID: %d) Cliente adicionado com sucesso!" % id_cliente)
                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_clientes == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-        Remover cliente        -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_cliente = ""
                encontrado = False
                while not encontrado:
                    id_cliente = ler_id("Digite o ID do cliente (ou 0 para cancelar): ")

                    if id_cliente == 0:
                        encontrado = True
                        continue

                    if id_cliente in clientes:
                        if clientes[id_cliente]["Ativo"]:
                            encontrado = True
                            print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                            print("Endereço:", clientes[id_cliente]["Endereco"])
                            print("Tem certeza que deseja remover esse cliente?")
                            decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                            if decisao.lower() == "s":
                                clientes[id_cliente]["Ativo"] = False
                                print("Cliente removido com sucesso!")
                        else:
                            print("Cliente inativo. (Já removido)")
                    else:
                        print("Não existe um cliente com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_clientes == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-       Atualizar cliente       -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_cliente = ""
                encontrado = False
                while not encontrado:
                    id_cliente = ler_id("Digite o ID do cliente (ou 0 para cancelar): ")

                    if id_cliente == 0:
                        encontrado = True
                        continue

                    if id_cliente in clientes:
                        if clientes[id_cliente]["Ativo"]:
                            encontrado = True
                            print("Informações antigas:")
                            print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                            print("Endereço:", clientes[id_cliente]["Endereco"])

                            print()
                            print("Informações novas:")
                            nome_cliente = input("Digite o nome do cliente: ")

                            print("Modelo de telefone: (00) 00000-0000")
                            tel_cliente = input("Digite o telefone do cliente: ")

                            email_cliente = input("Digite o e-mail do cliente: ")

                            endereco_cliente = input("Digite o endereço do cliente: ")

                            clientes[id_cliente] = {
                                "Nome": nome_cliente.title(),
                                "CPF": clientes[id_cliente]["CPF"],
                                "Telefone": tel_cliente,
                                "Email": email_cliente,
                                "Endereco": endereco_cliente,
                                "Ativo": True
                            }

                            print("Cliente atualizado com sucesso!")

                            print()
                            print("Informações novas:")
                            print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                            print("Endereço:", clientes[id_cliente]["Endereco"])
                        else:
                            print("Cliente inativo. (Removido)")
                    else:
                        print("Não existe um cliente com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

    elif resp == "3":

        resp_funcionarios = ""
        while resp_funcionarios != "0":
            os.system("cls" if os.name == "nt" else "clear")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-                               -|")
            print("|-     Módulo de Funcionários    -|")
            print("|-                               -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-  1 - Listar funcionários      -|")
            print("|-  2 - Adicionar funcionário    -|")
            print("|-  3 - Remover funcionário      -|")
            print("|-  4 - Atualizar funcionário    -|")
            print("|-  0 - Voltar                   -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            resp_funcionarios = input("Digite o número do submódulo que quer acessar: ")

            if resp_funcionarios == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-      Visualizar funcionário   -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                if len(funcionarios) > 0:
                    id_funcionario = ""
                    while id_funcionario != 0:
                        id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para cancelar): ")

                        if id_funcionario != 0:
                            if id_funcionario in funcionarios:
                                if funcionarios[id_funcionario]["Ativo"]:
                                    print()
                                    print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                                    print("Endereço:", funcionarios[id_funcionario]["Endereco"])
                                    print()
                                else:
                                    print()
                                    print(f"Funcionário com ID ({id_funcionario}) inativo. (Excluído)")
                                    print()
                            else:
                                print()
                                print(f"Funcionário com ID ({id_funcionario}) não encontrado.")
                                print()
                else:
                    print("Não existe nenhum funcionário cadastrado no sistema.")

                print()
                input("Aperte (ENTER) para continuar.")
                print()

            elif resp_funcionarios == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-      Adicionar funcionário    -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                nome_funcionario = input("Digite o nome do funcionário: ")
                cpf_funcionario = ler_cpf()

                print("Modelo de telefone: (00) 00000-0000")
                tel_funcionario = input("Digite o telefone do funcionário: ")

                email_funcionario = input("Digite o e-mail do funcionário: ")

                endereco_funcionario = input("Digite o endereço do funcionário: ")

                id_funcionario = 1
                if len(funcionarios) > 0:
                    id_funcionario = list(funcionarios.keys())[-1] + 1

                funcionarios[id_funcionario] = {
                    "Nome": nome_funcionario.title(),
                    "CPF": cpf_funcionario,
                    "Telefone": tel_funcionario,
                    "Email": email_funcionario,
                    "Endereco": endereco_funcionario,
                    "Ativo": True
                }

                print("(ID: %d) Funcionário adicionado com sucesso!" % id_funcionario)
                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_funcionarios == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-       Remover funcionário     -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_funcionario = ""
                encontrado = False
                while not encontrado:
                    id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para cancelar): ")

                    if id_funcionario == 0:
                        encontrado = True
                        continue

                    if id_funcionario in funcionarios:
                        if funcionarios[id_funcionario]["Ativo"]:
                            encontrado = True
                            print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                            print("Endereço:", funcionarios[id_funcionario]["Endereco"])
                            print("Tem certeza que deseja remover esse funcionário?")
                            decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                            if decisao.lower() == "s":
                                funcionarios[id_funcionario]["Ativo"] = False
                                print("Funcionário removido com sucesso!")
                        else:
                            print("Funcionário inativo. (Já removido)")
                    else:
                        print("Não existe um funcionário com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_funcionarios == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                               -|")
                print("|-      Atualizar funcionário    -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_funcionario = ""
                encontrado = False
                while not encontrado:
                    id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para cancelar): ")

                    if id_funcionario == 0:
                        encontrado = True
                        continue

                    if id_funcionario in funcionarios:
                        if funcionarios[id_funcionario]["Ativo"]:
                            encontrado = True
                            print("Informações antigas:")
                            print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                            print("Endereço:", funcionarios[id_funcionario]["Endereco"])

                            print()
                            print("Informações novas:")
                            nome_funcionario = input("Digite o nome do funcionário: ")

                            print("Modelo de telefone: (00) 00000-0000")
                            tel_funcionario = input("Digite o telefone do funcionário: ")

                            email_funcionario = input("Digite o e-mail do funcionário: ")

                            endereco_funcionario = input("Digite o endereço do funcionário: ")

                            funcionarios[id_funcionario] = {
                                "Nome": nome_funcionario.title(),
                                "CPF": funcionarios[id_funcionario]["CPF"],
                                "Telefone": tel_funcionario,
                                "Email": email_funcionario,
                                "Endereco": endereco_funcionario,
                                "Ativo": True
                            }

                            print("Funcionário atualizado com sucesso!")

                            print()
                            print("Informações novas:")
                            print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                            print("Endereço:", funcionarios[id_funcionario]["Endereco"])
                        else:
                            print("Funcionário inativo. (Removido)")
                    else:
                        print("Não existe um funcionário com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

    elif resp == "4":

        resp_locacoes = ""
        while resp_locacoes != "0":
            os.system("cls" if os.name == "nt" else "clear")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-                                   -|")
            print("|-         Módulo de Locações        -|")
            print("|-                                   -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-  1 - Listar locações              -|")
            print("|-  2 - Adicionar locação            -|")
            print("|-  3 - Remover locação              -|")
            print("|-  4 - Atualizar locação            -|")
            print("|-  0 - Voltar                       -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            resp_locacoes = input("Digite o número do submódulo que quer acessar: ")

            if resp_locacoes == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                                   -|")
                print("|-        Visualizar locação         -|")
                print("|-                                   -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                if len(locacoes) > 0:
                    id_locacao = ""
                    while id_locacao != 0:
                        id_locacao = ler_id("Digite o ID da locação (ou 0 para cancelar): ")

                        if id_locacao != 0:
                            if id_locacao in locacoes:
                                if locacoes[id_locacao]["Ativo"]:
                                    if locacoes[id_locacao]["ID_Cliente"] in clientes:
                                        nome_cliente_loc = clientes[locacoes[id_locacao]["ID_Cliente"]]["Nome"]
                                    else:
                                        nome_cliente_loc = "Cliente não encontrado"

                                    if locacoes[id_locacao]["ID_Produto"] in roupas:
                                        nome_produto_loc = roupas[locacoes[id_locacao]["ID_Produto"]]["Nome"]
                                    else:
                                        nome_produto_loc = "Produto não encontrado"

                                    print()
                                    print(f"Locação > ID: {id_locacao} | Cliente: {nome_cliente_loc} (ID: {locacoes[id_locacao]['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {locacoes[id_locacao]['ID_Produto']})")
                                    print(f"Check-in: {locacoes[id_locacao]['CheckIn']} | Check-out: {locacoes[id_locacao]['CheckOut']}")
                                    print()
                                else:
                                    print()
                                    print(f"Locação com ID ({id_locacao}) inativa. (Excluída)")
                                    print()
                            else:
                                print()
                                print(f"Locação com ID ({id_locacao}) não encontrada.")
                                print()
                else:
                    print("Não existe nenhuma locação cadastrada no sistema.")

                print()
                input("Aperte (ENTER) para continuar.")
                print()

            elif resp_locacoes == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                                   -|")
                print("|-         Adicionar locação         -|")
                print("|-                                   -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_cliente_loc = ler_id_existente("Digite o ID do cliente: ", clientes, "Não existe um cliente com esse ID.")
                id_produto_loc = ler_id_existente("Digite o ID do produto: ", roupas, "Não existe um produto com esse ID.")

                print("Formato de data: DD/MM/AAAA")
                checkin_loc = input("Digite a data de Check-in: ")

                checkout_loc = input("Digite a data de Check-out: ")

                id_locacao = 1
                if len(locacoes) > 0:
                    id_locacao = list(locacoes.keys())[-1] + 1

                locacoes[id_locacao] = {
                    "ID_Cliente": id_cliente_loc,
                    "ID_Produto": id_produto_loc,
                    "CheckIn": checkin_loc,
                    "CheckOut": checkout_loc,
                    "Ativo": True
                }

                print("(ID: %d) Locação adicionada com sucesso!" % id_locacao)
                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_locacoes == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                                   -|")
                print("|-          Remover locação          -|")
                print("|-                                   -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_locacao = ""
                encontrado = False
                while not encontrado:
                    id_locacao = ler_id("Digite o ID da locação (ou 0 para cancelar): ")

                    if id_locacao == 0:
                        encontrado = True
                        continue

                    if id_locacao in locacoes:
                        if locacoes[id_locacao]["Ativo"]:
                            encontrado = True
                            if locacoes[id_locacao]["ID_Cliente"] in clientes:
                                nome_cliente_loc = clientes[locacoes[id_locacao]["ID_Cliente"]]["Nome"]
                            else:
                                nome_cliente_loc = "Cliente não encontrado"

                            if locacoes[id_locacao]["ID_Produto"] in roupas:
                                nome_produto_loc = roupas[locacoes[id_locacao]["ID_Produto"]]["Nome"]
                            else:
                                nome_produto_loc = "Produto não encontrado"

                            print(f"Locação > ID: {id_locacao} | Cliente: {nome_cliente_loc} (ID: {locacoes[id_locacao]['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {locacoes[id_locacao]['ID_Produto']})")
                            print(f"Check-in: {locacoes[id_locacao]['CheckIn']} | Check-out: {locacoes[id_locacao]['CheckOut']}")
                            print("Tem certeza que deseja remover essa locação?")
                            decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                            if decisao.lower() == "s":
                                locacoes[id_locacao]["Ativo"] = False
                                print("Locação removida com sucesso!")
                        else:
                            print("Locação inativa. (Já removida)")
                    else:
                        print("Não existe uma locação com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_locacoes == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print("|-                                   -|")
                print("|-         Atualizar locação         -|")
                print("|-                                   -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                id_locacao = ""
                encontrado = False
                while not encontrado:
                    id_locacao = ler_id("Digite o ID da locação (ou 0 para cancelar): ")

                    if id_locacao == 0:
                        encontrado = True
                        continue

                    if id_locacao in locacoes:
                        if locacoes[id_locacao]["Ativo"]:
                            encontrado = True
                            if locacoes[id_locacao]["ID_Cliente"] in clientes:
                                nome_cliente_loc = clientes[locacoes[id_locacao]["ID_Cliente"]]["Nome"]
                            else:
                                nome_cliente_loc = "Cliente não encontrado"

                            if locacoes[id_locacao]["ID_Produto"] in roupas:
                                nome_produto_loc = roupas[locacoes[id_locacao]["ID_Produto"]]["Nome"]
                            else:
                                nome_produto_loc = "Produto não encontrado"

                            print("Informações antigas:")
                            print(f"Locação > ID: {id_locacao} | Cliente: {nome_cliente_loc} (ID: {locacoes[id_locacao]['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {locacoes[id_locacao]['ID_Produto']})")
                            print(f"Check-in: {locacoes[id_locacao]['CheckIn']} | Check-out: {locacoes[id_locacao]['CheckOut']}")

                            print()
                            print("Informações novas:")

                            id_cliente_loc = ler_id_existente("Digite o ID do cliente: ", clientes, "Não existe um cliente com esse ID.")
                            id_produto_loc = ler_id_existente("Digite o ID do produto: ", roupas, "Não existe um produto com esse ID.")

                            print("Formato de data: DD/MM/AAAA")
                            checkin_loc = input("Digite a data de Check-in: ")

                            checkout_loc = input("Digite a data de Check-out: ")

                            locacoes[id_locacao] = {
                                "ID_Cliente": id_cliente_loc,
                                "ID_Produto": id_produto_loc,
                                "CheckIn": checkin_loc,
                                "CheckOut": checkout_loc,
                                "Ativo": True
                            }

                            print("Locação atualizada com sucesso!")

                            if locacoes[id_locacao]["ID_Cliente"] in clientes:
                                nome_cliente_loc = clientes[locacoes[id_locacao]["ID_Cliente"]]["Nome"]
                            else:
                                nome_cliente_loc = "Cliente não encontrado"

                            if locacoes[id_locacao]["ID_Produto"] in roupas:
                                nome_produto_loc = roupas[locacoes[id_locacao]["ID_Produto"]]["Nome"]
                            else:
                                nome_produto_loc = "Produto não encontrado"

                            print()
                            print("Informações novas:")
                            print(f"Locação > ID: {id_locacao} | Cliente: {nome_cliente_loc} (ID: {locacoes[id_locacao]['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {locacoes[id_locacao]['ID_Produto']})")
                            print(f"Check-in: {locacoes[id_locacao]['CheckIn']} | Check-out: {locacoes[id_locacao]['CheckOut']}")
                        else:
                            print("Locação inativa. (Removida)")
                    else:
                        print("Não existe uma locação com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

    elif resp == "5":
        os.system("cls" if os.name == "nt" else "clear")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("|-                               -|")
        print("|-      Módulo de Relatórios     -|")
        print("|-                               -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print()
        print("Total de produtos cadastrados  :", len(roupas))
        print("Total de clientes cadastrados  :", len(clientes))
        print("Total de funcionários cadastrados:", len(funcionarios))
        print("Total de locações cadastradas  :", len(locacoes))
        print()
        input("Aperte (ENTER) para retornar.")
        print()

    elif resp == "6":
        os.system("cls" if os.name == "nt" else "clear")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("|-                               -|")
        print("|-        Sobre o Sistema        -|")
        print("|-                               -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print()
        print("Fantasy Wardrobe")
        print("Sistema de gerenciamento de locação de roupas e fantasias.")
        print()
        input("Aperte (ENTER) para retornar.")
        print()
        


roupasArquivo = open("roupas.dat", "wb")
pickle.dump(roupas, roupasArquivo)
roupasArquivo.close()

clientesArquivo = open("clientes.dat", "wb")
pickle.dump(clientes, clientesArquivo)
clientesArquivo.close()

funcionariosArquivo = open("funcionarios.dat", "wb")
pickle.dump(funcionarios, funcionariosArquivo)
funcionariosArquivo.close()

locacoesArquivo = open("locacoes.dat", "wb")
pickle.dump(locacoes, locacoesArquivo)
locacoesArquivo.close()