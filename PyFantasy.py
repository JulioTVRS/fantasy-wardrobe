import os

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
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("|-                                        -|")
    print("|-            Fantasy Wardrobe            -|")
    print("|-                                        -|")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("|-        1 - Roupas e Fantasias          -|")
    print("|-        2 - Clientes                    -|")
    print("|-        3 - Funcionários                -|")
    print("|-        4 - Gerenciar Locação           -|")
    print("|-        0 - Sair do sistema             -|")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    resp = input("Digite o número do módulo que quer acessar: ")

    if resp == "1":

        resp_roupas = ""
        while resp_roupas != "0":
            
            os.system("cls" if os.name == "nt" else "clear")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-                                      -|")
            print("|-            Módulo de Roupas          -|")
            print("|-               e Fantasias            -|")
            print("|-                                      -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-     1 - Listar todos os produtos     -|")
            print("|-     2 - Adicionar produtos           -|")
            print("|-     3 - Remover produtos             -|")
            print("|-     0 - Voltar                       -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

            resp_roupas = input("Digite o número do submódulo que quer acessar: ")

            if resp_roupas == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                -|")
                print("|-        Todas as Roupas         -|")
                print("|-           e Fantasias          -|")
                print("|-                                -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                
                if len(roupas) > 0:
                    for key, value in roupas.items():
                        print("Produto > ID:", key,"-", value["Nome"], "| Tamanho:", value["Tamanho"], "| Valor: R$", value["Valor"], "| Categoria:", value["Categoria"])
                else:
                    print("Não existe nenhum produto cadastrado no sistema.")
                   
                print()
                input("Aperte (ENTER) para continuar.")
                print()

            elif resp_roupas == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-      Adicionar produto     -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                
                nome_produto = input("Digite o nome do produto: ")
                
                while True:
                    try:
                        valor_produto = float(input("Digite o valor do produto: "))
                    except ValueError:
                        print()
                        print("Erro: Digite um número válido.")
                        continue

                    if valor_produto < 0:
                        print()
                        print("Erro: O valor do produto não pode ser negativo.")
                        continue

                    break
                
                desc_produto = input("Digite a descrição do produto: ")
                print("Padrão de tamanhos: (PP, P, M, G, GG, XG)")
                tam_produto = input("Digite o tamanho do produto: ")
                
                while tam_produto.lower() not in ["pp", "p", "m", "g", "gg", "xg"]:
                    print()
                    print("Tamanho inválido. Tente novamente! Tamanhos válidos: (PP, P, M, G, GG, XG)")
                    tam_produto = input("Digite o tamanho do produto: ")
                    
                print("Categorias válidas: Comum (1), Fantasia (2)")
                ctg_produto = input("Digite o número da categoria do produto: ")
                
                while ctg_produto != "1" and ctg_produto != "2":
                    print()
                    print("Categoria inválida. Tente novamente! Categorias válidas: Comum (1), Fantasia (2)")
                    ctg_produto = input("Digite o número da categoria do produto: ")
                    
                if ctg_produto == "1":
                    ctg_produto = "Comum"
                else:
                    ctg_produto = "Fantasia"
                
                id_produto = 1
                
                if len(roupas) > 0:
                    id_produto = list(roupas.keys())[-1] + 1
                    
                roupas[id_produto] = {
                    "Nome": nome_produto.capitalize(),
                    "Valor": valor_produto,
                    "Descricao": desc_produto,
                    "Tamanho": tam_produto.upper(),
                    "Categoria": ctg_produto
                }
                print("(ID: %d) Produto adicionado com sucesso!"%(id_produto))

                print()
                input("Aperte (ENTER) para continuar.")
                print()
            elif resp_roupas == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-       Remover produto      -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                
                id_produto = ""
                while id_produto != 0:
                    while True:
                        try:
                            id_produto = int(input("Digite o ID do produto (ou 0 para cancelar): "))
                            print()
                        except ValueError:
                            print()
                            print("Erro: Um ID consiste apenas em números.")
                            continue
                        break

                    if id_produto in roupas:
                        print("Produto > ID:", id_produto,"-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                        print("Tem certeza que deseja remover esse produto?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")
                        
                        if decisao.lower() == "s":
                            del roupas[id_produto]
                            break
                    else:
                        if id_produto != 0:
                            print("Não existe um produto com esse ID.")
                        break

                print()
                input("Aperte (ENTER) para continuar.")
                print()
    
    elif resp == "2":
        
        resp_clientes = ""
        while resp_clientes != "0":
            os.system("cls" if os.name == "nt" else "clear")
            
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-                                      -|")
            print("|-          Módulo de Clientes          -|")
            print("|-                                      -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-     1 - Listar todos os clientes     -|")
            print("|-     2 - Adicionar clientes           -|")
            print("|-     3 - Remover clientes             -|")
            print("|-     0 - Voltar                       -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
            resp_clientes = input("Digite o número do submódulo que quer acessar: ")
            
            if resp_clientes == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-      Todos os clientes     -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                
                if len(clientes) > 0:
                    for key, value in clientes.items():
                        print("Cliente > ID:", key,"-", value["Nome"], "| CPF:", value["CPF"], "| Telefone:", value["Telefone"], "| E-mail:", value["Email"])
                        print("Endereço:", value["Endereco"])
                else:
                    print("Não existe nenhum cliente cadastrado no sistema.")
                    
                print()
                input("Aperte (ENTER) para continuar.")
                print()
                
            elif resp_clientes == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-     Adicionar clientes     -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                
                nome_cliente = input("Digite o nome do cliente: ")
                
                cpf_cliente = input("Digite o CPF do cliente (apenas números): ")
                while len(cpf_cliente) != 11:
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
                
                print("(ID: %d) Cliente adicionado com sucesso!"%(id_cliente))
                
                print()
                input("Aperte (ENTER) para retornar.")
                print()
        
            elif resp_clientes == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-      Remover clientes      -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                
                id_cliente = ""
                while id_cliente != 0:
                    while True:
                        try:
                            id_cliente = int(input("Digite o ID do cliente (ou 0 para cancelar): "))
                            print()
                        except ValueError:
                            print()
                            print("Erro: Um ID consiste apenas em números.")
                            continue
                        break

                    if id_cliente in clientes:
                        print("Cliente > ID:", id_cliente,"-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                        print("Endereço:", clientes[id_cliente]["Endereco"])
                        print("Tem certeza que deseja remover esse cliente?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")
                        
                        if decisao.lower() == "s":
                            del clientes[id_cliente]
                            break
                    else:
                        if id_cliente != 0:
                            print("Não existe um cliente com esse ID.")
                        break
                
                print()
                input("Aperte (ENTER) para retornar.")
                print()

    elif resp == "3":
        
        resp_funcionarios = ""
        while resp_funcionarios != "0":
            os.system("cls" if os.name == "nt" else "clear")
            
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-                                          -|")
            print("|-          Módulo de Funcionários          -|")
            print("|-                                          -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-     1 - Listar todos os funcionários     -|")
            print("|-     2 - Adicionar funcionários           -|")
            print("|-     3 - Remover funcionários             -|")
            print("|-     0 - Voltar                           -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            
            resp_funcionarios = input("Digite o número do submódulo que quer acessar: ")
            
            if resp_funcionarios == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                  -|")
                print("|-      Todos os Funcionários       -|")
                print("|-                                  -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
 
                if len(funcionarios) > 0:
                    for key, value in funcionarios.items():
                        print("> ID:", key, "-", value["Nome"], "| CPF:", value["CPF"], "| Telefone:", value["Telefone"], "| E-mail:", value["Email"])
                        print("Endereço:", value["Endereco"])
                else:
                    print("Não existe nenhum funcionário cadastrado no sistema.")
                    
                print()
                input("Aperte (ENTER) para continuar.")
                print()
            
            elif resp_funcionarios == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                  -|")
                print("|-      Adicionar funcionário       -|")
                print("|-                                  -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
 
                nome_funcionario = input("Digite o nome do funcionário: ")
 
                cpf_funcionario = input("Digite o CPF do funcionário (apenas números): ")
                while len(cpf_funcionario) != 11:
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
 
                print("(ID: %d) Funcionário adicionado com sucesso!"%(id_funcionario))
 
                print()
                input("Aperte (ENTER) para retornar.")
                print()
            elif resp_funcionarios == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                  -|")
                print("|-       Remover funcionário        -|")
                print("|-                                  -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
 
                id_funcionario = ""
                while id_funcionario != 0:
                    while True:
                        try:
                            id_funcionario = int(input("Digite o ID do funcionário (ou 0 para cancelar): "))
                            print()
                        except ValueError:
                            print()
                            print("Erro: Um ID consiste apenas em números.")
                            continue
                        break
 
                    if id_funcionario in funcionarios:
                        print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                        print("Endereço:", funcionarios[id_funcionario]["Endereco"])
                        print("Tem certeza que deseja remover esse funcionário?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")
 
                        if decisao.lower() == "s":
                            del funcionarios[id_funcionario]
                            break
                    else:
                        if id_funcionario != 0:
                            print("Não existe um funcionário com esse ID.")
                        break
 
                print()
                input("Aperte (ENTER) para retornar.")
                print()        
                

    elif resp == "4":
        
        resp_locacoes = ""
        while resp_locacoes != "0":
            os.system("cls" if os.name == "nt" else "clear")
            
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-                                        -|")
            print("|-           Módulo de Locações           -|")
            print("|-                                        -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-     1 - Listar todas as locações       -|")
            print("|-     2 - Adicionar locação              -|")
            print("|-     3 - Remover locação                -|")
            print("|-     0 - Voltar                         -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

            resp_locacoes = input("Digite o número do submódulo que quer acessar: ")
 
            if resp_locacoes == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                  -|")
                print("|-       Todas as Locações          -|")
                print("|-                                  -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
 
                if len(locacoes) > 0:
                    for key, value in locacoes.items():
                        if value["ID_Cliente"] in clientes:
                            nome_cliente_locacao = clientes[value["ID_Cliente"]]["Nome"]
                        else:
                            nome_cliente_locacao = "Cliente Excluído"
                            
                        if value["ID_Produto"] in roupas:
                            nome_produto_locacao = roupas[value["ID_Produto"]]["Nome"]
                        else:
                            nome_produto_locacao = "Produto Excluído" 
                            
                        print("Locação > ID:", key, "| Cliente:", nome_cliente_locacao, "(ID:", str(value["ID_Cliente"]) + ")", "| Produto:", nome_produto_locacao, "(ID:", str(value["ID_Produto"]) + ")")
                        print("Check-in:", value["CheckIn"], "| Check-out:", value["CheckOut"])
                else:
                    print("Não existe nenhuma locação cadastrada no sistema.")
 
                print()
                input("Aperte (ENTER) para continuar.")
                print()
                
            elif resp_locacoes == "2":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                  -|")
                print("|-         Adicionar Locações       -|")
                print("|-                                  -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                  -|")
                print("|-         Em Desenvolvimento       -|")
                print("|-                                  -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                
                print()
                input("Aperte (ENTER) para continuar.")
                print()
                
            elif resp_locacoes == "3":
                os.system("cls" if os.name == "nt" else "clear")
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                  -|")
                print("|-         Remover Locações         -|")
                print("|-                                  -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                  -|")
                print("|-         Em Desenvolvimento       -|")
                print("|-                                  -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                
                print()
                input("Aperte (ENTER) para continuar.")
                print()
