from arquivos import recuperar_roupas, recuperar_clientes, recuperar_funcionarios, recuperar_locacoes
from utils import mostrar_menu, mostrar_submenu, limpar

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
        else:
            print("Opção inválida!")
            print()
            input("Aperte (ENTER) para continuar.")
            print()
        
        