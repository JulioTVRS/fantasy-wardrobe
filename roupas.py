import os
import pickle
from arquivos import recuperar_roupas, gravar_roupas

from utils import ler_id, menu, submenu

def ler_valor():
    while True:
        try:
            valor = float(input("Digite o valor do produto: "))
        except ValueError:
            print("Erro: Digite um número válido.")
            continue

        if valor < 0:
            print("Erro: O valor do produto não pode ser negativo.")
            continue

        return valor


def ler_tamanho():
    print("Padrão de tamanhos: (PP, P, M, G, GG, XG)")
    tamanho = input("Digite o tamanho do produto: ")
    while tamanho.lower() not in ["pp", "p", "m", "g", "gg", "xg"]:
        print("Tamanho inválido. Tente novamente! Tamanhos válidos: (PP, P, M, G, GG, XG)")
        tamanho = input("Digite o tamanho do produto: ")
    return tamanho.upper()


def ler_categoria():
    print("Categorias válidas: Comum (1), Fantasia (2)")
    categoria = input("Digite o número da categoria do produto: ")
    while categoria != "1" and categoria != "2":
        print("Categoria inválida. Tente novamente! Categorias válidas: Comum (1), Fantasia (2)")
        categoria = input("Digite o número da categoria do produto: ")

    if categoria == "1":
        return "Comum"
    else:
        return "Fantasia"

def ModuloRoupas():
        roupas = recuperar_roupas()
    
        resp_roupas = ""
        while resp_roupas != "0":
            os.system("cls" if os.name == "nt" else "clear")
            print(menu("Módulo de Roupas e Fantasias", [
                "1 - Listar produto",
                "2 - Adicionar produto",
                "3 - Remover produto",
                "4 - Atualizar produto",
                "0 - Voltar"
            ]))

            resp_roupas = input("Digite o número do submódulo que quer acessar: ")

            if resp_roupas == "1":
                os.system("cls" if os.name == "nt" else "clear")
                submenu("Visualizar produto")
                
                if len(roupas) > 0:
                    id_produto = ""
                    while id_produto != 0:
                        id_produto = ler_id("Digite o ID do produto (ou 0 para voltar): ")

                        if id_produto != 0:
                            if id_produto in roupas:
                                if roupas[id_produto]["Ativo"]:
                                    print()
                                    print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                                    print("Descrição:", roupas[id_produto]["Descricao"])
                                    print()
                                else:
                                    print()
                                    print(f"Produto com ID ({id_produto}) inativo. (Excluído)")
                                    print()
                            else:
                                print()
                                print(f"Produto com ID ({id_produto}) não encontrado.")
                                print()
                else:
                    print("Não existe nenhum produto cadastrado no sistema.")

                print()
                input("Aperte (ENTER) para continuar.")
                print()

            elif resp_roupas == "2":
                os.system("cls" if os.name == "nt" else "clear")
                submenu("Adicionar produto")

                nome_produto = input("Digite o nome do produto: ")
                valor_produto = ler_valor()
                desc_produto = input("Digite a descrição do produto: ")
                tam_produto = ler_tamanho()
                ctg_produto = ler_categoria()

                id_produto = 1
                if len(roupas) > 0:
                    id_produto = list(roupas.keys())[-1] + 1

                roupas[id_produto] = {
                    "Nome": nome_produto.capitalize(),
                    "Valor": valor_produto,
                    "Descricao": desc_produto,
                    "Tamanho": tam_produto,
                    "Categoria": ctg_produto,
                    "Ativo": True
                }

                gravar_roupas(roupas)

                print("(ID: %d) Produto adicionado com sucesso!" % id_produto)
                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_roupas == "3":
                os.system("cls" if os.name == "nt" else "clear")
                submenu("Remover produto")

                id_produto = ""
                encontrado = False
                while not encontrado:
                    id_produto = ler_id("Digite o ID do produto (ou 0 para voltar): ")

                    if id_produto == 0:
                        encontrado = True
                        continue

                    if id_produto in roupas:
                        encontrado = True
                        print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                        print("Descrição:", roupas[id_produto]["Descricao"])
                        print("Tem certeza que deseja remover esse produto?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                        if decisao.lower() == "s":
                            roupas[id_produto]["Ativo"] = False
                            gravar_roupas(roupas)
                            print("Produto removido com sucesso!")
                    else:
                        print("Não existe um produto com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()

            elif resp_roupas == "4":
                os.system("cls" if os.name == "nt" else "clear")
                submenu("Atualizar produto")

                id_produto = ""
                encontrado = False
                while not encontrado:
                    id_produto = ler_id("Digite o ID do produto (ou 0 para voltar): ")

                    if id_produto == 0:
                        encontrado = True
                        continue

                    if id_produto in roupas:
                        if roupas[id_produto]["Ativo"]:
                            encontrado = True
                            print("Informações antigas:")
                            print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                            print("Descrição:", roupas[id_produto]["Descricao"])

                            print()
                            print("Informações novas:")
                            nome_produto = input("Digite o nome do produto: ")
                            valor_produto = ler_valor()
                            desc_produto = input("Digite a descrição do produto: ")
                            tam_produto = ler_tamanho()
                            ctg_produto = ler_categoria()

                            roupas[id_produto] = {
                                "Nome": nome_produto.capitalize(),
                                "Valor": valor_produto,
                                "Descricao": desc_produto,
                                "Tamanho": tam_produto,
                                "Categoria": ctg_produto,
                                "Ativo": True
                            }
                            
                            gravar_roupas(roupas)
                            print("Produto atualizado com sucesso!")
                            
                            print()
                            print("Informações novas:")
                            print("Produto > ID:", id_produto, "-", roupas[id_produto]["Nome"], "| Tamanho:", roupas[id_produto]["Tamanho"], "| Valor: R$", roupas[id_produto]["Valor"], "| Categoria:", roupas[id_produto]["Categoria"])
                            print("Descrição:", roupas[id_produto]["Descricao"])
                        else:
                            print("Produto inativo. (Removido)")
                    else:
                        print("Não existe um produto com esse ID.")

                print()
                input("Aperte (ENTER) para retornar.")
                print()