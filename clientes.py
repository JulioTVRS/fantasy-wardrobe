import os
from arquivos import recuperar_clientes, gravar_clientes
from utils import ler_id, ler_cpf, menu, submenu

def ModuloClientes():
    clientes = recuperar_clientes()
    
    resp_clientes = ""
    while resp_clientes != "0":
        os.system("cls" if os.name == "nt" else "clear")
        menu("Módulo de Clientes", [
            "1 - Listar clientes",
            "2 - Adicionar cliente",
            "3 - Remover cliente",
            "4 - Atualizar cliente",
            "0 - Voltar"
        ])

        resp_clientes = input("Digite o número do submódulo que quer acessar: ")

        if resp_clientes == "1":
            os.system("cls" if os.name == "nt" else "clear")
            submenu("Visualizar cliente")

            if len(clientes) > 0:
                id_cliente = ""
                while id_cliente != 0:
                    id_cliente = ler_id("Digite o ID do cliente (ou 0 para voltar): ")

                    if id_cliente != 0:
                        if id_cliente in clientes:
                            if clientes[id_cliente]["Ativo"]:
                                print()
                                print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                                print("Endereço:", clientes[id_cliente]["Endereco"])
                                print()
                            else:
                                print()
                                print(f"Cliente com ID ({id_cliente}) inativo. (Excluído)")
                                print()
                        else:
                            print()
                            print(f"Cliente com ID ({id_cliente}) não encontrado.")
                            print()
            else:
                print("Não existe nenhum cliente cadastrado no sistema.")

            print()
            input("Aperte (ENTER) para continuar.")
            print()

        elif resp_clientes == "2":
            os.system("cls" if os.name == "nt" else "clear")
            submenu("Adicionar cliente")

            nome_cliente = input("Digite o nome do cliente: ")
            cpf_cliente = ler_cpf()

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
                "Endereco": endereco_cliente,
                "Ativo": True
            }

            gravar_clientes(clientes)

            print("(ID: %d) Cliente adicionado com sucesso!" % id_cliente)
            print()
            input("Aperte (ENTER) para retornar.")
            print()

        elif resp_clientes == "3":
            os.system("cls" if os.name == "nt" else "clear")
            submenu("Remover cliente")

            id_cliente = ""
            encontrado = False
            while not encontrado:
                id_cliente = ler_id("Digite o ID do cliente (ou 0 para voltar): ")

                if id_cliente == 0:
                    encontrado = True
                    continue

                if id_cliente in clientes:
                    if clientes[id_cliente]["Ativo"]:
                        encontrado = True
                        print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                        print("Endereço:", clientes[id_cliente]["Endereco"])
                        print("Tem certeza que deseja remover esse cliente?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                        if decisao.lower() == "s":
                            clientes[id_cliente]["Ativo"] = False
                            gravar_clientes(clientes)
                            print("Cliente removido com sucesso!")
                    else:
                        print("Cliente inativo. (Já removido)")
                else:
                    print("Não existe um cliente com esse ID.")

            print()
            input("Aperte (ENTER) para retornar.")
            print()

        elif resp_clientes == "4":
            os.system("cls" if os.name == "nt" else "clear")
            submenu("Atualizar cliente")

            id_cliente = ""
            encontrado = False
            while not encontrado:
                id_cliente = ler_id("Digite o ID do cliente (ou 0 para voltar): ")

                if id_cliente == 0:
                    encontrado = True
                    continue

                if id_cliente in clientes:
                    if clientes[id_cliente]["Ativo"]:
                        encontrado = True
                        print("Informações antigas:")
                        print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                        print("Endereço:", clientes[id_cliente]["Endereco"])

                        print()
                        print("Informações novas:")
                        nome_cliente = input("Digite o nome do cliente: ")

                        print("Modelo de telefone: (00) 00000-0000")
                        tel_cliente = input("Digite o telefone do cliente: ")

                        email_cliente = input("Digite o e-mail do cliente: ")

                        endereco_cliente = input("Digite o endereço do cliente: ")

                        clientes[id_cliente] = {
                            "Nome": nome_cliente.title(),
                            "CPF": clientes[id_cliente]["CPF"],
                            "Telefone": tel_cliente,
                            "Email": email_cliente,
                            "Endereco": endereco_cliente,
                            "Ativo": True
                        }

                        gravar_clientes(clientes)
                        print("Cliente atualizado com sucesso!")

                        print()
                        print("Informações novas:")
                        print("Cliente > ID:", id_cliente, "-", clientes[id_cliente]["Nome"], "| CPF:", clientes[id_cliente]["CPF"], "| Telefone:", clientes[id_cliente]["Telefone"], "| E-mail:", clientes[id_cliente]["Email"])
                        print("Endereço:", clientes[id_cliente]["Endereco"])
                    else:
                        print("Cliente inativo. (Removido)")
                else:
                    print("Não existe um cliente com esse ID.")

            print()
            input("Aperte (ENTER) para retornar.")
            print()