from arquivos import recuperar_roupas, recuperar_clientes, recuperar_funcionarios, recuperar_locacoes
from utils import mostrar_menu, mostrar_submenu

def ModuloRelatorios():
    resp_relatorios = ""
    while resp_relatorios != "0":
        mostrar_menu("Módulo de Relatórios", [
            "1 - Listar todos os clientes",
            "2 - Listar clientes pelo nome"
            "3 - Listar clientes aniversariantes (do mês)",
            "4 - Listar locações ativas",
            "5 - Atualizar produto",
            "0 - Voltar"
        ])
        
        resp_roupas = input("Digite o número do relatório que quer gerar: ")
        
        