from arquivos import recuperar_roupas, recuperar_clientes, recuperar_funcionarios, recuperar_locacoes
from utils import mostrar_menu, mostrar_submenu, limpar
from validacao import ler_nome

def ListarTodosClientes(clientes):
    limpar()
    mostrar_submenu("Listando todos os clientes")
    
    print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
    print(f"┃ {"ID":^10} ┃   Nome completo                        ┃   CPF          ┃  E-mail                              ┃")
    print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
    for id, value in clientes.items():
        if value["Ativo"]:
            print(f"┃ {str(id).center(10)} ┃ {value["Nome"]:<38} ┃ {value["CPF"]:^14} ┃ {value["Email"]:<36} ┃")
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
        if nome_pesquisa.lower().strip() in value["Nome"].lower() and value["Ativo"]:
            encontrados[id] = value

    if len(encontrados) > 0:
        print()
        print(f"┏┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓")
        print(f"┃ {"ID":^10} ┃   Nome completo                        ┃   CPF          ┃  E-mail                              ┃")
        print(f"┣┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╋┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┫")
        for id, value in encontrados.items():
            print(f"┃ {str(id).center(10)} ┃ {value["Nome"]:<38} ┃ {value["CPF"]:^14} ┃ {value["Email"]:<36} ┃")
        print(f"┗┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┻┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛")
    else:
        print()
        print("Nenhum cliente encontrado com esse nome.")

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
            "5 - Locações ativas",
            "6 - Locações pelo cliente",
            "0 - Voltar"
        ])
        
        resp_relatorios = input("Digite o número do relatório que quer gerar: ")
        
        if resp_relatorios == "1":
            ListarTodosClientes(clientes)
        elif resp_relatorios == "2":
            ListarClientesPeloNome(clientes)
        
        