from datetime import date, datetime
from arquivos import recuperar_locacoes, recuperar_roupas, recuperar_clientes, gravar_locacoes
from utils import mostrar_menu, mostrar_submenu, limpar
from validacao import ler_id

def ler_id_existente(mensagem, dicionario, mensagem_erro):
    valor = ler_id(mensagem)
    while valor not in dicionario:
        print(mensagem_erro)
        valor = ler_id(mensagem)
    return valor

def ler_data(mensagem, mensagem_erro):
    data = input(mensagem)
    verificado = False
    
    while not verificado:
        try:
            datamodelo = datetime.strptime(data, "%d/%m/%Y").date()
            
            if datamodelo >= date.today():
                verificado = True
            else:
                print(mensagem_erro)
                data = input(mensagem)
                
        except ValueError:
            print(mensagem_erro)
            data = input(mensagem)
            
    return data
    

def ModuloLocacoes():
    locacoes = recuperar_locacoes()
    roupas = recuperar_roupas()
    clientes = recuperar_clientes()
    
    resp_locacoes = ""
    while resp_locacoes != "0":
        limpar()
        mostrar_menu("Módulo de Funcionários", [
            "1 - Listar locações",
            "2 - Adicionar locação",
            "3 - Remover locação",
            "4 - Atualizar locação",
            "0 - Voltar"
        ])

        resp_locacoes = input("Digite o número do submódulo que quer acessar: ")

        if resp_locacoes == "1":
            limpar()
            mostrar_submenu("Visualizar locação")

            if len(locacoes) > 0:
                id_locacao = ""
                while id_locacao != 0:
                    id_locacao = ler_id("Digite o ID da locação (ou 0 para voltar): ")

                    if id_locacao != 0:
                        if id_locacao in locacoes:
                            if locacoes[id_locacao]["Ativo"]:
                                if locacoes[id_locacao]["ID_Cliente"] in clientes:
                                    nome_cliente_loc = clientes[locacoes[id_locacao]["ID_Cliente"]]["Nome"]
                                else:
                                    nome_cliente_loc = "Cliente não encontrado"

                                if locacoes[id_locacao]["ID_Produto"] in roupas:
                                    nome_produto_loc = roupas[locacoes[id_locacao]["ID_Produto"]]["Nome"]
                                else:
                                    nome_produto_loc = "Produto não encontrado"

                                print()
                                print(f"Locação > ID: {id_locacao} | Cliente: {nome_cliente_loc} (ID: {locacoes[id_locacao]['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {locacoes[id_locacao]['ID_Produto']})")
                                print(f"Check-in: {locacoes[id_locacao]['CheckIn']} | Check-out: {locacoes[id_locacao]['CheckOut']}")
                                print()
                            else:
                                print()
                                print(f"Locação com ID ({id_locacao}) inativa. (Excluída)")
                                print()
                        else:
                            print()
                            print(f"Locação com ID ({id_locacao}) não encontrada.")
                            print()
            else:
                print("Não existe nenhuma locação cadastrada no sistema.")

            print()
            input("Aperte (ENTER) para continuar.")
            print()

        elif resp_locacoes == "2":
            limpar()
            mostrar_submenu("Adicionar locação")

            id_cliente_loc = ler_id_existente("Digite o ID do cliente: ", clientes, "Não existe um cliente com esse ID.")
            id_produto_loc = ler_id_existente("Digite o ID do produto: ", roupas, "Não existe um produto com esse ID.")

            checkin_loc = str(date.today().day) + "/" + str(date.today().month) + "/" + str(date.today().year)

            print("Formato de data: DD/MM/AAAA")

            checkout_loc = ler_data("Digite a data de Check-out: ", "Data inválida, tente novamente!")

            id_locacao = 1
            if len(locacoes) > 0:
                id_locacao = list(locacoes.keys())[-1] + 1

            locacoes[id_locacao] = {
                "ID_Cliente": id_cliente_loc,
                "ID_Produto": id_produto_loc,
                "CheckIn": checkin_loc,
                "CheckOut": checkout_loc,
                "Ativo": True
            }

            gravar_locacoes(locacoes)

            print("(ID: %d) Locação adicionada com sucesso!" % id_locacao)
            print()
            input("Aperte (ENTER) para retornar.")
            print()

        elif resp_locacoes == "3":
            limpar()
            mostrar_submenu("Remover locação")

            id_locacao = ""
            encontrado = False
            while not encontrado:
                id_locacao = ler_id("Digite o ID da locação (ou 0 para voltar): ")

                if id_locacao == 0:
                    encontrado = True
                    continue

                if id_locacao in locacoes:
                    if locacoes[id_locacao]["Ativo"]:
                        encontrado = True
                        if locacoes[id_locacao]["ID_Cliente"] in clientes:
                            nome_cliente_loc = clientes[locacoes[id_locacao]["ID_Cliente"]]["Nome"]
                        else:
                            nome_cliente_loc = "Cliente não encontrado"

                        if locacoes[id_locacao]["ID_Produto"] in roupas:
                            nome_produto_loc = roupas[locacoes[id_locacao]["ID_Produto"]]["Nome"]
                        else:
                            nome_produto_loc = "Produto não encontrado"

                        print(f"Locação > ID: {id_locacao} | Cliente: {nome_cliente_loc} (ID: {locacoes[id_locacao]['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {locacoes[id_locacao]['ID_Produto']})")
                        print(f"Check-in: {locacoes[id_locacao]['CheckIn']} | Check-out: {locacoes[id_locacao]['CheckOut']}")
                        print("Tem certeza que deseja remover essa locação?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                        if decisao.lower() == "s":
                            locacoes[id_locacao]["Ativo"] = False
                            gravar_locacoes(locacoes)
                            print("Locação removida com sucesso!")
                            
                    else:
                        print("Locação inativa. (Já removida)")
                else:
                    print("Não existe uma locação com esse ID.")

            print()
            input("Aperte (ENTER) para retornar.")
            print()

        elif resp_locacoes == "4":
            limpar()
            mostrar_submenu("Atualizar locação")

            id_locacao = ""
            encontrado = False
            while not encontrado:
                id_locacao = ler_id("Digite o ID da locação (ou 0 para voltar): ")

                if id_locacao == 0:
                    encontrado = True
                    continue

                if id_locacao in locacoes:
                    if locacoes[id_locacao]["Ativo"]:
                        encontrado = True
                        if locacoes[id_locacao]["ID_Cliente"] in clientes:
                            nome_cliente_loc = clientes[locacoes[id_locacao]["ID_Cliente"]]["Nome"]
                        else:
                            nome_cliente_loc = "Cliente não encontrado"

                        if locacoes[id_locacao]["ID_Produto"] in roupas:
                            nome_produto_loc = roupas[locacoes[id_locacao]["ID_Produto"]]["Nome"]
                        else:
                            nome_produto_loc = "Produto não encontrado"

                        print("Informações antigas:")
                        print(f"Locação > ID: {id_locacao} | Cliente: {nome_cliente_loc} (ID: {locacoes[id_locacao]['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {locacoes[id_locacao]['ID_Produto']})")
                        print(f"Check-in: {locacoes[id_locacao]['CheckIn']} | Check-out: {locacoes[id_locacao]['CheckOut']}")

                        print()
                        print("Informações novas:")

                        id_cliente_loc = ler_id_existente("Digite o ID do cliente: ", clientes, "Não existe um cliente com esse ID.")
                        id_produto_loc = ler_id_existente("Digite o ID do produto: ", roupas, "Não existe um produto com esse ID.")

                        print("Formato de data: DD/MM/AAAA")
                        checkin_loc = input("Digite a data de Check-in: ")

                        checkout_loc = ler_data("Digite a data de Check-out: ", "Data inválida, tente novamente!")

                        locacoes[id_locacao] = {
                            "ID_Cliente": id_cliente_loc,
                            "ID_Produto": id_produto_loc,
                            "CheckIn": checkin_loc,
                            "CheckOut": checkout_loc,
                            "Ativo": True
                        }

                        gravar_locacoes(locacoes)

                        print("Locação atualizada com sucesso!")

                        if locacoes[id_locacao]["ID_Cliente"] in clientes:
                            nome_cliente_loc = clientes[locacoes[id_locacao]["ID_Cliente"]]["Nome"]
                        else:
                            nome_cliente_loc = "Cliente não encontrado"

                        if locacoes[id_locacao]["ID_Produto"] in roupas:
                            nome_produto_loc = roupas[locacoes[id_locacao]["ID_Produto"]]["Nome"]
                        else:
                            nome_produto_loc = "Produto não encontrado"

                        print()
                        print("Informações novas:")
                        print(f"Locação > ID: {id_locacao} | Cliente: {nome_cliente_loc} (ID: {locacoes[id_locacao]['ID_Cliente']}) | Produto: {nome_produto_loc} (ID: {locacoes[id_locacao]['ID_Produto']})")
                        print(f"Check-in: {locacoes[id_locacao]['CheckIn']} | Check-out: {locacoes[id_locacao]['CheckOut']}")
                    else:
                        print("Locação inativa. (Removida)")
                else:
                    print("Não existe uma locação com esse ID.")

            print()
            input("Aperte (ENTER) para retornar.")
            print()