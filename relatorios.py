from datetime import datetime, date
from arquivos import recuperar_roupas, recuperar_clientes, recuperar_funcionarios, recuperar_locacoes
from utils import mostrar_menu, mostrar_submenu, limpar, data_atual
from validacao import ler_nome, ler_id_existente

def ListarTodosClientes(clientes):
    limpar()
    mostrar_submenu("Listando todos os clientes")
    
    print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
    print(f"┃     ID     ┃   Nome completo                        ┃   CPF          ┃   E-mail                             ┃")
    print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
    for id, value in clientes.items():
        if value["Ativo"]:
            print(f"┃ {str(id).center(10)} ┃ {value['Nome']:<38} ┃ {value['CPF']:^14} ┃ {value['Email']:<36} ┃")
    print(f"┗┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")
        
    print()
    input("Aperte (ENTER) para continuar.")
    print()
    
def ListarClientesPeloNome(clientes):
    limpar()
    mostrar_submenu("Listando clientes pelo nome")

    nome_pesquisa = ler_nome("Digite o nome (ou parte do nome) do cliente: ", "O nome não pode ser vazio, tente novamente!")

    encontrados = {}
    for id, value in clientes.items():
        if nome_pesquisa.lower().strip() in value['Nome'].lower() and value['Ativo']:
            encontrados[id] = value

    if len(encontrados) > 0:
        print()
        print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
        print(f"┃     ID     ┃   Nome completo                        ┃   CPF          ┃  E-mail                              ┃")
        print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
        for id, value in encontrados.items():
            print(f"┃ {str(id).center(10)} ┃ {value['Nome']:<38} ┃ {value['CPF']:^14} ┃ {value['Email']:<36} ┃")
        print(f"┗┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")
    else:
        print()
        print("Nenhum cliente encontrado com esse nome.")

    print()
    input("Aperte (ENTER) para continuar.")
    print()

def ListarClientesAniversariantes(clientes):
    limpar()
    mostrar_submenu("Listando clientes aniversariantes")

    encontrados = {}
    
    for id, value in clientes.items():
        if value["Ativo"]:
            cliente_mes_nasc = value["DataNascimento"].split("/")[1]
            hoje = data_atual().split("/")[1]

            if cliente_mes_nasc == hoje:
                encontrados[id] = value

    if len(encontrados) > 0:
        print()
        print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
        print(f"┃     ID     ┃   Nome completo                        ┃   CPF          ┃  E-mail                              ┃  Data de Nasc. ┃")
        print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
        for id, value in encontrados.items():
            print(f"┃ {str(id).center(10)} ┃ {value['Nome']:<38} ┃ {value['CPF']:^14} ┃ {value['Email']:<36} ┃ {value["DataNascimento"]:^14} ┃")
        print(f"┗┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")
    else:
        print()
        print("Nenhum cliente faz aniversário este mês.")

    print()
    input("Aperte (ENTER) para continuar.")
    print()

def ListarFuncionariosAniversariantes(funcionarios):
    limpar()
    mostrar_submenu("Listando funcionários aniversariantes")

    encontrados = {}
    
    for id, value in funcionarios.items():
        if value["Ativo"]:
            funcionario_mes_nasc = value["DataNascimento"].split("/")[1]
            hoje = data_atual().split("/")[1]

            if funcionario_mes_nasc == hoje:
                encontrados[id] = value

    if len(encontrados) > 0:
        print()
        print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
        print(f"┃     ID     ┃   Nome completo                        ┃   CPF          ┃  E-mail                              ┃  Data de Nasc. ┃")
        print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
        for id, value in encontrados.items():
            print(f"┃ {str(id).center(10)} ┃ {value['Nome']:<38} ┃ {value['CPF']:^14} ┃ {value['Email']:<36} ┃ {value["DataNascimento"]:^14} ┃")
        print(f"┗┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")
    else:
        print()
        print("Nenhum funcionário faz aniversário este mês.")

    print()
    input("Aperte (ENTER) para continuar.")
    print()

def ListarTodasLocacoes(locacoes, clientes, roupas):
    limpar()
    mostrar_submenu("Listando todas as locações")

    encontrados = {}

    for id, value in locacoes.items():
        if value["Ativo"]:
            encontrados[id] = value

    if len(encontrados) > 0:
        print()
        print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
        print(f"┃     ID     ┃   Nome do produto              ┃   Nome do cliente              ┃  Data Check-IN   ┃  Data Check-OUT  ┃")
        print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
        for id, value in encontrados.items():
            ID_Produto = value["ID_Produto"]
            ID_Cliente = value['ID_Cliente']
            print(f"┃ {str(id).center(10)} ┃ {roupas[ID_Produto]["Nome"]:<30} ┃ {clientes[ID_Cliente]["Nome"]:<30} ┃ {value["CheckIn"]:^16} ┃ {value["CheckOut"]:^16} ┃")
        print(f"┗┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")
    else:
        print()
        print("Nenhuma locação ativa encontrada.")

    print()
    input("Aperte (ENTER) para continuar.")
    print()

def ListarLocacoesPendentes(locacoes, clientes, roupas):
    limpar()
    mostrar_submenu("Listando locações pendentes")

    hoje = datetime.strptime(data_atual(), "%d/%m/%Y").date()

    encontrados = {}

    for id, value in locacoes.items():
        if value["Ativo"]:
            checkout = datetime.strptime(value["CheckOut"], "%d/%m/%Y").date()

            if checkout >= hoje:
                encontrados[id] = value

    if len(encontrados) > 0:
        print()
        print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
        print(f"┃     ID     ┃   Nome do produto              ┃   Nome do cliente              ┃  Data Check-IN   ┃  Data Check-OUT  ┃")
        print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
        for id, value in encontrados.items():
            ID_Produto = value["ID_Produto"]
            ID_Cliente = value['ID_Cliente']
            print(f"┃ {str(id).center(10)} ┃ {roupas[ID_Produto]["Nome"]:<30} ┃ {clientes[ID_Cliente]["Nome"]:<30} ┃ {value["CheckIn"]:^16} ┃ {value["CheckOut"]:^16} ┃")
        print(f"┗┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")
    else:
        print()
        print("Nenhuma locação ativa encontrada.")

    print()
    input("Aperte (ENTER) para continuar.")
    print()

def ListarLocacoesPeloCliente(locacoes, clientes, roupas):
    limpar()
    mostrar_submenu("Listando locações pelo cliente")

    nome_pesquisa = ler_nome("Digite o nome (ou parte do nome) do cliente: ", "O nome não pode ser vazio, tente novamente!")

    encontrados = {}
    for id, value in clientes.items():
        if nome_pesquisa.lower().strip() in value['Nome'].lower() and value['Ativo']:
            encontrados[id] = value
            
    if len(encontrados) > 0:
        print()
        print("Clientes encontrados:")
        for id, value in encontrados.items():
            print(f"ID: {id} - {value['Nome']}")

        id_pesquisa = ler_id_existente("Digite o ID do cliente: ", clientes, "Não existe um cliente com esse ID.")

        locacoespesquisa = {}

        for id, value in locacoes.items():
            if value["ID_Cliente"] == id_pesquisa:
                locacoespesquisa[id] = value
            
        if len(locacoespesquisa) > 0:
            limpar()
            mostrar_submenu("Listando locações pelo cliente")

            print()
            print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
            print(f"┃     ID     ┃   Nome do produto              ┃   Nome do cliente              ┃  Data Check-IN   ┃  Data Check-OUT  ┃")
            print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
            for id, value in locacoespesquisa.items():
                ID_Produto = value["ID_Produto"]
                ID_Cliente = value['ID_Cliente']
                print(f"┃ {str(id).center(10)} ┃ {roupas[ID_Produto]["Nome"]:<30} ┃ {clientes[ID_Cliente]["Nome"]:<30} ┃ {value["CheckIn"]:^16} ┃ {value["CheckOut"]:^16} ┃")
            print(f"┗┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")
        else:
            print()
            print("Nenhuma locação ativa encontrada.")

    else:
        print("Não foi encontrado ninguém com esse nome.")

    print()
    input("Aperte (ENTER) para continuar.")
    print()
    



def ModuloRelatorios():
    limpar()
    roupas = recuperar_roupas()
    clientes = recuperar_clientes()
    funcionarios = recuperar_funcionarios()
    locacoes = recuperar_locacoes()
    
    resp_relatorios = ""
    while resp_relatorios != "0":
        limpar()
        mostrar_menu("Módulo de Relatórios", [
            "1 - Listar todos os clientes",
            "2 - Listar clientes pelo nome",
            "3 - Clientes aniversariantes (do mês)",
            "4 - Funcionários aniversariantes (do mês)",
            "5 - Listar todas as locações",
            "6 - Locações pendentes",
            "7 - Locações pelo cliente",
            "0 - Voltar"
        ])
        
        resp_relatorios = input("Digite o número do relatório que quer gerar: ")
        
        if resp_relatorios == "1":
            ListarTodosClientes(clientes)

        elif resp_relatorios == "2":
            ListarClientesPeloNome(clientes)

        elif resp_relatorios == "3":
            ListarClientesAniversariantes(clientes)
        
        elif resp_relatorios == "4":
            ListarFuncionariosAniversariantes(funcionarios)

        elif resp_relatorios == "5":
            ListarTodasLocacoes(locacoes, clientes, roupas)

        elif resp_relatorios == "6":
            ListarLocacoesPendentes(locacoes, clientes, roupas)

        elif resp_relatorios == "7":
            ListarLocacoesPeloCliente(locacoes, clientes, roupas)
        