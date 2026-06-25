import os
import pickle

from utils import menu
from arquivos import recuperar_clientes, recuperar_funcionarios, recuperar_locacoes, recuperar_roupas, gravar_roupas, gravar_clientes, gravar_funcionarios, gravar_locacoes
from roupas import ModuloRoupas
from clientes import ModuloClientes
from funcionarios import ModuloFuncionarios
from locacoes import ModuloLocacoes

resp = ""
while resp != "0":
    funcionarios = recuperar_funcionarios()
    roupas = recuperar_roupas()
    clientes = recuperar_clientes()
    locacoes = recuperar_locacoes()
    
    os.system("cls" if os.name == "nt" else "clear")
    print(menu("Fantasy Wardrobe", [
        "1 - Roupas e Fantasias",
        "2 - Clientes",
        "3 - Funcionários",
        "4 - Gerenciar Locação",
        "5 - Relatórios",
        "6 - Sobre o Sistema",
        "0 - Sair"
    ]))

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
    else:
        print()
        print("Opção inválida!")
        input("Aperte (ENTER) para retornar.")
        

gravar_roupas(roupas)
gravar_clientes(clientes)
gravar_funcionarios(funcionarios)
gravar_locacoes(locacoes)