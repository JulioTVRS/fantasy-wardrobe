import os

#Os 4 dicionários abaixo fazem parte de uma estrutura de dados ficticia, para dar ideia de como estarão funcionando no sistema
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
            print("|-  1 - Listar produtos          -|")
            print("|-  2 - Adicionar produtos       -|")
            print("|-  3 - Remover produtos         -|")
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
                print("Lista de produtos:")
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
                valor_produto = input("Digite o valor do produto: ")
                desc_produto = input("Digite a descrição do produto: ")
                print("Padrão de tamanhos: (PP, P, M, G, GG, XG)")
                tam_produto = input("Digite o tamanho do produto: ")
                print("Categorias válidas: Comum (1), Fantasia (2)")
                ctg_produto = input("Digite o número da categoria do produto: ")

                id_produto = list(roupas.keys())[-1] + 1

                print()
                print("(ID: %d) Produto adicionado com sucesso!" % id_produto)
                print()
                input("Aperte (ENTER) para continuar.")
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

                id_produto = input("Digite o ID do produto (ou 0 para cancelar): ")

                if id_produto != 0:
                    decisao = input("Tem certeza? (S para remover): ")
                    if decisao.lower() == "s":
                        print("Produto removido com sucesso!")

                print()
                input("Aperte (ENTER) para continuar.")
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
            print("|-  2 - Adicionar clientes       -|")
            print("|-  3 - Remover clientes         -|")
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
                print("Lista de clientes:")
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
                print("Modelo de telefone: (00) 00000-0000")
                tel_cliente = input("Digite o telefone do cliente: ")
                email_cliente = input("Digite o e-mail do cliente: ")
                endereco_cliente = input("Digite o endereço do cliente: ")

                id_cliente = list(clientes.keys())[-1] + 1

                print()
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

                id_cliente = input("Digite o ID do cliente (ou 0 para cancelar): ")

                if id_cliente != 0:
                    decisao = input("Tem certeza? (S para remover): ")
                    if decisao.lower() == "s":
                        print("Cliente removido com sucesso!")

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
            print("|-  2 - Adicionar funcionários   -|")
            print("|-  3 - Remover funcionários     -|")
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
                print("Lista de funcionários:")
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
                print("Modelo de telefone: (00) 00000-0000")
                tel_funcionario = input("Digite o telefone do funcionário: ")
                email_funcionario = input("Digite o e-mail do funcionário: ")
                endereco_funcionario = input("Digite o endereço do funcionário: ")

                id_funcionario = list(funcionarios.keys())[-1] + 1

                print()
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

                id_funcionario = int(input("Digite o ID do funcionário (ou 0 para cancelar): "))

                if id_funcionario != 0:
                    decisao = input("Tem certeza? (S para remover): ")
                    if decisao.lower() == "s":
                        print("Funcionário removido com sucesso!")

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
                print("Lista de locações:")
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
                id_produto_loc = input("Digite o ID do produto: ")
                print("Formato de data: DD/MM/AAAA")
                checkin_loc = input("Digite a data de Check-in: ")
                checkout_loc = input("Digite a data de Check-out: ")

                id_locacao = list(locacoes.keys())[-1] + 1

                print()
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

                id_locacao = input("Digite o ID da locação (ou 0 para cancelar): ")

                if id_locacao != 0:
                    decisao = input("Tem certeza? (S para remover): ")
                    if decisao.lower() == "s":
                        print("Locação removida com sucesso!")

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
        print("Relatórios do sistema:")
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