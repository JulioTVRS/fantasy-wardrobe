import os
from arquivos import recuperar_funcionarios, gravar_funcionarios
from utils import ler_id, ler_cpf

funcionarios = recuperar_funcionarios()

def ModuloFuncionarios():
    resp_funcionarios = ""
    while resp_funcionarios != "0":
        os.system("cls" if os.name == "nt" else "clear")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("|-                               -|")
        print("|-     Módulo de Funcionários    -|")
        print("|-                               -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("|-  1 - Listar funcionários      -|")
        print("|-  2 - Adicionar funcionário    -|")
        print("|-  3 - Remover funcionário      -|")
        print("|-  4 - Atualizar funcionário    -|")
        print("|-  0 - Voltar                   -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        resp_funcionarios = input("Digite o número do submódulo que quer acessar: ")

        if resp_funcionarios == "1":
            os.system("cls" if os.name == "nt" else "clear")
            print()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-                               -|")
            print("|-      Visualizar funcionário   -|")
            print("|-                               -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()

            if len(funcionarios) > 0:
                id_funcionario = ""
                while id_funcionario != 0:
                    id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para cancelar): ")

                    if id_funcionario != 0:
                        if id_funcionario in funcionarios:
                            if funcionarios[id_funcionario]["Ativo"]:
                                print()
                                print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                                print("Endereço:", funcionarios[id_funcionario]["Endereco"])
                                print()
                            else:
                                print()
                                print(f"Funcionário com ID ({id_funcionario}) inativo. (Excluído)")
                                print()
                        else:
                            print()
                            print(f"Funcionário com ID ({id_funcionario}) não encontrado.")
                            print()
            else:
                print("Não existe nenhum funcionário cadastrado no sistema.")

            print()
            input("Aperte (ENTER) para continuar.")
            print()

        elif resp_funcionarios == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-                               -|")
            print("|-      Adicionar funcionário    -|")
            print("|-                               -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()

            nome_funcionario = input("Digite o nome do funcionário: ")
            cpf_funcionario = ler_cpf()

            print("Modelo de telefone: (00) 00000-0000")
            tel_funcionario = input("Digite o telefone do funcionário: ")

            email_funcionario = input("Digite o e-mail do funcionário: ")

            endereco_funcionario = input("Digite o endereço do funcionário: ")

            id_funcionario = 1
            if len(funcionarios) > 0:
                id_funcionario = list(funcionarios.keys())[-1] + 1

            funcionarios[id_funcionario] = {
                "Nome": nome_funcionario.title(),
                "CPF": cpf_funcionario,
                "Telefone": tel_funcionario,
                "Email": email_funcionario,
                "Endereco": endereco_funcionario,
                "Ativo": True
            }

            gravar_funcionarios(funcionarios)

            print("(ID: %d) Funcionário adicionado com sucesso!" % id_funcionario)
            print()
            input("Aperte (ENTER) para retornar.")
            print()

        elif resp_funcionarios == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-                               -|")
            print("|-       Remover funcionário     -|")
            print("|-                               -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()

            id_funcionario = ""
            encontrado = False
            while not encontrado:
                id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para cancelar): ")

                if id_funcionario == 0:
                    encontrado = True
                    continue

                if id_funcionario in funcionarios:
                    if funcionarios[id_funcionario]["Ativo"]:
                        encontrado = True
                        print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                        print("Endereço:", funcionarios[id_funcionario]["Endereco"])
                        print("Tem certeza que deseja remover esse funcionário?")
                        decisao = input("(S para Remover ou Qualquer outra tecla para cancelar): ")

                        if decisao.lower() == "s":
                            funcionarios[id_funcionario]["Ativo"] = False
                            gravar_funcionarios(funcionarios)
                            print("Funcionário removido com sucesso!")
                    else:
                        print("Funcionário inativo. (Já removido)")
                else:
                    print("Não existe um funcionário com esse ID.")

            print()
            input("Aperte (ENTER) para retornar.")
            print()

        elif resp_funcionarios == "4":
            os.system("cls" if os.name == "nt" else "clear")
            print()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("|-                               -|")
            print("|-      Atualizar funcionário    -|")
            print("|-                               -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()

            id_funcionario = ""
            encontrado = False
            while not encontrado:
                id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para cancelar): ")

                if id_funcionario == 0:
                    encontrado = True
                    continue

                if id_funcionario in funcionarios:
                    if funcionarios[id_funcionario]["Ativo"]:
                        encontrado = True
                        print("Informações antigas:")
                        print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                        print("Endereço:", funcionarios[id_funcionario]["Endereco"])

                        print()
                        print("Informações novas:")
                        nome_funcionario = input("Digite o nome do funcionário: ")

                        print("Modelo de telefone: (00) 00000-0000")
                        tel_funcionario = input("Digite o telefone do funcionário: ")

                        email_funcionario = input("Digite o e-mail do funcionário: ")

                        endereco_funcionario = input("Digite o endereço do funcionário: ")

                        funcionarios[id_funcionario] = {
                            "Nome": nome_funcionario.title(),
                            "CPF": funcionarios[id_funcionario]["CPF"],
                            "Telefone": tel_funcionario,
                            "Email": email_funcionario,
                            "Endereco": endereco_funcionario,
                            "Ativo": True
                        }

                        gravar_funcionarios(funcionarios)

                        print("Funcionário atualizado com sucesso!")

                        print()
                        print("Informações novas:")
                        print("Funcionário > ID:", id_funcionario, "-", funcionarios[id_funcionario]["Nome"], "| CPF:", funcionarios[id_funcionario]["CPF"], "| Telefone:", funcionarios[id_funcionario]["Telefone"], "| E-mail:", funcionarios[id_funcionario]["Email"])
                        print("Endereço:", funcionarios[id_funcionario]["Endereco"])
                    else:
                        print("Funcionário inativo. (Removido)")
                else:
                    print("Não existe um funcionário com esse ID.")

            print()
            input("Aperte (ENTER) para retornar.")
            print()
