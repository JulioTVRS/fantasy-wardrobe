import os
import pickle

from arquivos import recuperar_clientes, recuperar_funcionarios, recuperar_locacoes, recuperar_roupas
from roupas import ModuloRoupas
from clientes import ModuloClientes
from funcionarios import ModuloFuncionarios
from locacoes import ModuloLocacoes

funcionarios = recuperar_funcionarios()
roupas = recuperar_roupas()
clientes = recuperar_clientes()
locacoes = recuperar_locacoes()


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