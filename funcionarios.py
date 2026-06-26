from arquivos import recuperar_funcionarios, gravar_funcionarios
from utils import mostrar_menu, mostrar_submenu, limpar
from validacao import ler_email, ler_id, ler_cpf, ler_nome

def ListarFuncionarios(funcionarios):
    limpar()
    mostrar_submenu("Visualizar funcionário")

    if len(funcionarios) > 0:
        id_funcionario = ""
        while id_funcionario != 0:
            id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para voltar): ")

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
    
def AdicionarFuncionarios(funcionarios):
    limpar()
    mostrar_submenu("Adicionar funcionário")

    nome_funcionario = ler_nome("Digite o nome do funcionário: ", "O nome não pode ser vazio, tente novamente!")
    cpf_funcionario = ler_cpf()

    print("Modelo de telefone: (00) 00000-0000")
    tel_funcionario = input("Digite o telefone do funcionário: ")

    email_funcionario = ler_email("Digite o e-mail do funcionário: ", "E-mail inválido, tente novamente!")

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
    
def RemoverFuncionarios(funcionarios):
    limpar()
    mostrar_submenu("Remover funcionário")

    id_funcionario = ""
    encontrado = False
    while not encontrado:
        id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para voltar): ")

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
    
def AtualizarFuncionarios(funcionarios):
    limpar()
    mostrar_submenu("Atualizar funcionário")

    id_funcionario = ""
    encontrado = False
    while not encontrado:
        id_funcionario = ler_id("Digite o ID do funcionário (ou 0 para voltar): ")

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
                nome_funcionario = ler_nome("Digite o nome do funcionário: ", "O nome não pode ser vazio, tente novamente!")

                print("Modelo de telefone: (00) 00000-0000")
                tel_funcionario = input("Digite o telefone do funcionário: ")

                email_funcionario = ler_email("Digite o e-mail do funcionário: ", "E-mail inválido, tente novamente!")

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

def ModuloFuncionarios():
    resp_funcionarios = ""
    while resp_funcionarios != "0":
        funcionarios = recuperar_funcionarios()
        
        limpar()
        mostrar_menu("Módulo de Funcionários", [
            "1 - Listar funcionário",
            "2 - Adicionar funcionário",
            "3 - Remover funcionário",
            "4 - Atualizar funcionário",
            "0 - Voltar"
        ])

        resp_funcionarios = input("Digite o número do submódulo que quer acessar: ")

        if resp_funcionarios == "1":
            ListarFuncionarios(funcionarios)

        elif resp_funcionarios == "2":
            AdicionarFuncionarios(funcionarios)

        elif resp_funcionarios == "3":
            RemoverFuncionarios(funcionarios)

        elif resp_funcionarios == "4":
            AtualizarFuncionarios(funcionarios)