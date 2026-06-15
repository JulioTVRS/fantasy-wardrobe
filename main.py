import os
import pickle

# Dicionários já com dados para acelerar os testes

roupas = {              
    1: {
        "Nome": "Terno",
        "Valor": 80,
        "Descricao": "Terno preto com gravata.",
        "Tamanho": "G",
        "Categoria": "Comum"
    }
}

clientes = {
    1: {
        "Nome": "Fulano de Tal",
        "CPF": "12345678900",
        "Telefone": "(84) 12345-6789",
        "Email": "fulano5@gmail.com",
        "Endereco": "Rua das Palmeiras, 245, Lagoa Nova, Natal - RN, CEP 59075-320"
    }
}

funcionarios = {
    1: {
        "Nome": "Beltrano da Silva",
        "CPF": "98765432100",
        "Telefone": "(84) 54321-6789",
        "Email": "beltrano1@gmail.com",
        "Endereco": "Rua das Palmeiras, 246, Lagoa Nova, Natal - RN, CEP 59075-320"
    }
}

locacoes = {
    1: {
        "ID_Cliente": 1,
        "ID_Produto": 1,
        "CheckIn": "25/05/2026",
        "CheckOut": "30/06/2026"
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
                print("|-        Todas as Roupas        -|")
                print("|-          e Fantasias          -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                if len(roupas) > 0:
                    for key, value in roupas.items():
                        print("Produto > ID:", key, "-", value["Nome"], "| Tamanho:", value["Tamanho"], "| Valor: R$", value["Valor"], "| Categoria:", value["Categoria"])
                        print("Descrição:", value["Descricao"])
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

                while True:
                    try:
                        valor_produto = float(input("Digite o valor do produto: "))
                    except ValueError:
                        print("Erro: Digite um número válido.")
                        continue
                    if valor_produto < 0:
                        print("Erro: O valor do produto não pode ser negativo.")
                        continue
                    break

                desc_produto = input("Digite a descrição do produto: ")
                print("Padrão de tamanhos: (PP, P, M, G, GG, XG)")
                tam_produto = input("Digite o tamanho do produto: ")

                while tam_produto.lower() not in ["pp", "p", "m", "g", "gg", "xg"]:
                    print("Tamanho inválido. Tente novamente! Tamanhos válidos: (PP, P, M, G, GG, XG)")
                    tam_produto = input("Digite o tamanho do produto: ")

                print("Categorias válidas: Comum (1), Fantasia (2)")
                ctg_produto = input("Digite o número da categoria do produto: ")

                while ctg_produto != "1" and ctg_produto != "2":
                    print("Categoria inválida. Tente novamente! Categorias válidas: Comum (1), Fantasia (2)")
                    ctg_produto = input("Digite o número da categoria do produto: ")

                ctg_produto = "Comum" if ctg_produto == "1" else "Fantasia"

                id_produto = 1
                if len(roupas) > 0:
                    id_produto = list(roupas.keys())[-1] + 1
                    # O ID produto funciona devido aos dicionários serem ordenados por criação a partir do Python 3.7
                    # Basicamente ele pega o maior valor de ID e soma 1
                    # Adendos:
                    # 1 (Proposital) - Se houver X produtos, ex (ID 1, 2 e 3) o 2 for apagado e um novo for criado o ID será 4 ficarão apenas (1, 3, 4)
                    # 2 (Acidental, pode causar problemas futuros) - Se houver X produtos e o ultimo for apagado, ex (ID 1, 2, 3), o 3 sendo apagado, o próximo produto será 3, ficando (1, 2, 3)

                roupas[id_produto] = {
                    "Nome": nome_produto.capitalize(),
                    "Valor": valor_produto,
                    "Descricao": desc_produto,
                    "Tamanho": tam_produto.upper(),
                    "Categoria": ctg_produto
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

                while True:
                    id_produto = input("Digite o ID do produto (ou 0 para cancelar): ")
                    while not id_produto.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_produto = input("Digite o ID do produto (ou 0 para cancelar): ")

                    id_produto = int(id_produto)

                    if id_produto == 0:
                        break

                    if id_produto in roupas:
                        print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                        print("Descrição:", roupas[id_produto]["Descricao"])
                        print("Tem certeza que deseja remover esse produto?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                        if decisao.lower() == "s":
                            del roupas[id_produto]
                            print("Produto removido com sucesso!")
                        break
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

                while True:
                    id_produto = input("Digite o ID do produto (ou 0 para cancelar): ")
                    while not id_produto.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_produto = input("Digite o ID do produto (ou 0 para cancelar): ")

                    id_produto = int(id_produto)

                    if id_produto == 0:
                        break

                    if id_produto in roupas:
                        print("Informações antigas:")
                        print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                        print("Descrição:", roupas[id_produto]["Descricao"])

                        print()
                        print("Informações novas:")
                        nome_produto = input("Digite o nome do produto: ")

                        while True:
                            try:
                                valor_produto = float(input("Digite o valor do produto: "))
                            except ValueError:
                                print("Erro: Digite um número válido.")
                                continue
                            if valor_produto < 0:
                                print("Erro: O valor do produto não pode ser negativo.")
                                continue
                            break

                        desc_produto = input("Digite a descrição do produto: ")
                        print("Padrão de tamanhos: (PP, P, M, G, GG, XG)")
                        tam_produto = input("Digite o tamanho do produto: ")

                        while tam_produto.lower() not in ["pp", "p", "m", "g", "gg", "xg"]:
                            print("Tamanho inválido. Tente novamente! Tamanhos válidos: (PP, P, M, G, GG, XG)")
                            tam_produto = input("Digite o tamanho do produto: ")

                        print("Categorias válidas: Comum (1), Fantasia (2)")
                        ctg_produto = input("Digite o número da categoria do produto: ")

                        while ctg_produto != "1" and ctg_produto != "2":
                            print("Categoria inválida. Tente novamente! Categorias válidas: Comum (1), Fantasia (2)")
                            ctg_produto = input("Digite o número da categoria do produto: ")

                        ctg_produto = "Comum" if ctg_produto == "1" else "Fantasia"

                        roupas[id_produto] = {
                            "Nome": nome_produto.capitalize(),
                            "Valor": valor_produto,
                            "Descricao": desc_produto,
                            "Tamanho": tam_produto.upper(),
                            "Categoria": ctg_produto
                        }

                        print("Produto atualizado com sucesso!")
                        break
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
                print("|-      Todos os Clientes        -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                if len(clientes) > 0:
                    for key, value in clientes.items():
                        print("Cliente > ID:", key, "-", value["Nome"], "| CPF:", value["CPF"], "| Telefone:", value["Telefone"], "| E-mail:", value["Email"])
                        print("Endereço:", value["Endereco"])
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

                cpf_cliente = input("Digite o CPF do cliente (apenas números): ")
                while len(cpf_cliente) != 11 or not cpf_cliente.isdigit():
                    print("CPF inválido. Tente novamente.")
                    cpf_cliente = input("Digite o CPF do cliente (apenas números): ")

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
                    "Endereco": endereco_cliente
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

                while True:
                    id_cliente = input("Digite o ID do cliente (ou 0 para cancelar): ")
                    while not id_cliente.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_cliente = input("Digite o ID do cliente (ou 0 para cancelar): ")

                    id_cliente = int(id_cliente)

                    if id_cliente == 0:
                        break

                    if id_cliente in clientes:
                        print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                        print("Endereço:", clientes[id_cliente]["Endereco"])
                        print("Tem certeza que deseja remover esse cliente?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                        if decisao.lower() == "s":
                            del clientes[id_cliente]
                            print("Cliente removido com sucesso!")
                        break
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

                while True:
                    id_cliente = input("Digite o ID do cliente (ou 0 para cancelar): ")
                    while not id_cliente.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_cliente = input("Digite o ID do cliente (ou 0 para cancelar): ")

                    id_cliente = int(id_cliente)

                    if id_cliente == 0:
                        break

                    if id_cliente in clientes:
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
                            "Endereco": endereco_cliente
                        }

                        print("Cliente atualizado com sucesso!")
                        break
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
                print("|-      Todos os Funcionários    -|")
                print("|-                               -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                if len(funcionarios) > 0:
                    for key, value in funcionarios.items():
                        print("Funcionário > ID:", key, "-", value["Nome"], "| CPF:", value["CPF"], "| Telefone:", value["Telefone"], "| E-mail:", value["Email"])
                        print("Endereço:", value["Endereco"])
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

                cpf_funcionario = input("Digite o CPF do funcionário (apenas números): ")
                while len(cpf_funcionario) != 11 or not cpf_funcionario.isdigit():
                    print("CPF inválido. Tente novamente.")
                    cpf_funcionario = input("Digite o CPF do funcionário (apenas números): ")

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
                    "Endereco": endereco_funcionario
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

                while True:
                    id_funcionario = input("Digite o ID do funcionário (ou 0 para cancelar): ")
                    while not id_funcionario.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_funcionario = input("Digite o ID do funcionário (ou 0 para cancelar): ")

                    id_funcionario = int(id_funcionario)

                    if id_funcionario == 0:
                        break

                    if id_funcionario in funcionarios:
                        print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                        print("Endereço:", funcionarios[id_funcionario]["Endereco"])
                        print("Tem certeza que deseja remover esse funcionário?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                        if decisao.lower() == "s":
                            del funcionarios[id_funcionario]
                            print("Funcionário removido com sucesso!")
                        break
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

                while True:
                    id_funcionario = input("Digite o ID do funcionário (ou 0 para cancelar): ")
                    while not id_funcionario.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_funcionario = input("Digite o ID do funcionário (ou 0 para cancelar): ")

                    id_funcionario = int(id_funcionario)

                    if id_funcionario == 0:
                        break

                    if id_funcionario in funcionarios:
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
                            "Endereco": endereco_funcionario
                        }

                        print("Funcionário atualizado com sucesso!")
                        break
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
                print("|-         Todas as Locações         -|")
                print("|-                                   -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print()

                if len(locacoes) > 0:
                    for key, value in locacoes.items():
                        if value["ID_Cliente"] in clientes:
                            nome_cliente_loc = clientes[value["ID_Cliente"]]["Nome"]
                        else:
                            nome_cliente_loc = "Cliente não encontrado"

                        if value["ID_Produto"] in roupas:
                            nome_produto_loc = roupas[value["ID_Produto"]]["Nome"]
                        else:
                            nome_produto_loc = "Produto não encontrado"

                        print(f"Locação > ID: {key} | Cliente: {nome_cliente_loc} (ID: {value['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {value['ID_Produto']})")
                        print(f"Check-in: {value['CheckIn']} | Check-out: {value['CheckOut']}")
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

                id_cliente_loc = input("Digite o ID do cliente: ")
                while not id_cliente_loc.isdigit():
                    print("Erro: Um ID consiste apenas em números.")
                    id_cliente_loc = input("Digite o ID do cliente: ")

                while int(id_cliente_loc) not in clientes:
                    print("Não existe um cliente com esse ID.")
                    id_cliente_loc = input("Digite o ID do cliente: ")
                    while not id_cliente_loc.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_cliente_loc = input("Digite o ID do cliente: ")

                id_produto_loc = input("Digite o ID do produto: ")
                while not id_produto_loc.isdigit():
                    print("Erro: Um ID consiste apenas em números.")
                    id_produto_loc = input("Digite o ID do produto: ")

                while int(id_produto_loc) not in roupas:
                    print("Não existe um produto com esse ID.")
                    id_produto_loc = input("Digite o ID do produto: ")
                    while not id_produto_loc.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_produto_loc = input("Digite o ID do produto: ")

                print("Formato de data: DD/MM/AAAA")
                checkin_loc = input("Digite a data de Check-in: ")

                checkout_loc = input("Digite a data de Check-out: ")

                id_locacao = 1
                if len(locacoes) > 0:
                    id_locacao = list(locacoes.keys())[-1] + 1

                locacoes[id_locacao] = {
                    "ID_Cliente": int(id_cliente_loc),
                    "ID_Produto": int(id_produto_loc),
                    "CheckIn": checkin_loc,
                    "CheckOut": checkout_loc
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

                while True:
                    id_locacao = input("Digite o ID da locação (ou 0 para cancelar): ")
                    while not id_locacao.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_locacao = input("Digite o ID da locação (ou 0 para cancelar): ")

                    id_locacao = int(id_locacao)

                    if id_locacao == 0:
                        break

                    if id_locacao in locacoes:
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
                            del locacoes[id_locacao]
                            print("Locação removida com sucesso!")
                        break
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

                while True:
                    id_locacao = input("Digite o ID da locação (ou 0 para cancelar): ")
                    while not id_locacao.isdigit():
                        print("Erro: Um ID consiste apenas em números.")
                        id_locacao = input("Digite o ID da locação (ou 0 para cancelar): ")

                    id_locacao = int(id_locacao)

                    if id_locacao == 0:
                        break

                    if id_locacao in locacoes:
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

                        id_cliente_loc = input("Digite o ID do cliente: ")
                        while not id_cliente_loc.isdigit():
                            print("Erro: Um ID consiste apenas em números.")
                            id_cliente_loc = input("Digite o ID do cliente: ")

                        while int(id_cliente_loc) not in clientes:
                            print("Não existe um cliente com esse ID.")
                            id_cliente_loc = input("Digite o ID do cliente: ")
                            while not id_cliente_loc.isdigit():
                                print("Erro: Um ID consiste apenas em números.")
                                id_cliente_loc = input("Digite o ID do cliente: ")

                        id_produto_loc = input("Digite o ID do produto: ")
                        while not id_produto_loc.isdigit():
                            print("Erro: Um ID consiste apenas em números.")
                            id_produto_loc = input("Digite o ID do produto: ")

                        while int(id_produto_loc) not in roupas:
                            print("Não existe um produto com esse ID.")
                            id_produto_loc = input("Digite o ID do produto: ")
                            while not id_produto_loc.isdigit():
                                print("Erro: Um ID consiste apenas em números.")
                                id_produto_loc = input("Digite o ID do produto: ")

                        print("Formato de data: DD/MM/AAAA")
                        checkin_loc = input("Digite a data de Check-in: ")

                        checkout_loc = input("Digite a data de Check-out: ")

                        locacoes[id_locacao] = {
                            "ID_Cliente": int(id_cliente_loc),
                            "ID_Produto": int(id_produto_loc),
                            "CheckIn": checkin_loc,
                            "CheckOut": checkout_loc
                        }

                        print("Locação atualizada com sucesso!")
                        break
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