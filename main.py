from utils import mostrar_menu, limpar
from arquivos import *
from roupas import ModuloRoupas
from clientes import ModuloClientes
from funcionarios import ModuloFuncionarios
from locacoes import ModuloLocacoes
from relatorios import ModuloRelatorios

def Sistema():
    resp = ""
    while resp != "0":
        funcionarios = recuperar_funcionarios()
        roupas = recuperar_roupas()
        clientes = recuperar_clientes()
        locacoes = recuperar_locacoes()
        
        limpar()
        mostrar_menu("Fantasy Wardrobe", [
            "1 - Roupas e Fantasias",
            "2 - Clientes",
            "3 - Funcionários",
            "4 - Gerenciar Locação",
            "5 - Relatórios",
            "6 - Sobre o Sistema",
            "0 - Sair"
        ])

        resp = input("Digite o número do módulo que quer acessar: ")

        if resp == "1":
            ModuloRoupas()
            
        elif resp == "2":
            ModuloClientes()
            
        elif resp == "3":
            ModuloFuncionarios()
            
        elif resp == "4":
            ModuloLocacoes()

        elif resp == "5":
            ModuloRelatorios()

        elif resp == "6":
            limpar()
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
        elif resp == "0":
            print()
            print("Saindo do sistema!")
        else:
            print()
            print("Opção inválida!")
            input("Aperte (ENTER) para retornar.")
            
Sistema()
        

