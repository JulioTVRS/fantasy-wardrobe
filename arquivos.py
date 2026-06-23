import pickle

def recuperar_roupas():
    try:
        roupas = {}
        roupasArquivo = open("roupas.dat", "rb")
        roupas = pickle.load(roupasArquivo)
        roupasArquivo.close()
    except:
        roupas = {              
            1: {
                "Nome": "Terno",
                "Valor": 80,
                "Descricao": "Terno preto com gravata.",
                "Tamanho": "G",
                "Categoria": "Comum",
                "Ativo": True
            }
        }
        roupasArquivo = open("roupas.dat", "wb")
        pickle.dump(roupas, roupasArquivo)
        roupasArquivo.close()

    return roupas

def recuperar_clientes():
    try:
        clientesArquivo = open("clientes.dat", "rb")
        clientes = pickle.load(clientesArquivo)
        clientesArquivo.close()
    except:
        clientes = {
            1: {
                "Nome": "Fulano de Tal",
                "CPF": "12345678900",
                "Telefone": "(84) 12345-6789",
                "Email": "fulano5@gmail.com",
                "Endereco": "Rua das Palmeiras, 245, Lagoa Nova, Natal - RN, CEP 59075-320",
                "Ativo": True
            }
        }
        clientesArquivo = open("clientes.dat", "wb")
        pickle.dump(clientes, clientesArquivo)
        clientesArquivo.close()

    return clientes

def recuperar_funcionarios():
    try:
        funcionariosArquivo = open("funcionarios.dat", "rb")
        funcionarios = pickle.load(funcionariosArquivo)
        funcionariosArquivo.close()
    except:
        funcionarios = {
            1: {
                "Nome": "Beltrano da Silva",
                "CPF": "98765432100",
                "Telefone": "(84) 54321-6789",
                "Email": "beltrano1@gmail.com",
                "Endereco": "Rua das Palmeiras, 246, Lagoa Nova, Natal - RN, CEP 59075-320",
                "Ativo": True
            }
        }
        funcionariosArquivo = open("funcionarios.dat", "wb")
        pickle.dump(funcionarios, funcionariosArquivo)
        funcionariosArquivo.close()

    return funcionarios

def recuperar_locacoes():
    try:
        locacoesArquivo = open("locacoes.dat", "rb")
        locacoes = pickle.load(locacoesArquivo)
        locacoesArquivo.close()
    except:
        locacoes = {
            1: {
                "ID_Cliente": 1,
                "ID_Produto": 1,
                "CheckIn": "25/05/2026",
                "CheckOut": "30/06/2026",
                "Ativo": True
            }
        }
        locacoesArquivo = open("locacoes.dat", "wb")
        pickle.dump(locacoes, locacoesArquivo)
        locacoesArquivo.close()

    return locacoes

def gravar_roupas(roupas):
    roupasArquivo = open("roupas.dat", "wb")
    pickle.dump(roupas, roupasArquivo)
    roupasArquivo.close()

def gravar_clientes(clientes):
    clientesArquivo = open("clientes.dat", "wb")
    pickle.dump(clientes, clientesArquivo)
    clientesArquivo.close()

def gravar_funcionarios(funcionarios):
    funcionariosArquivo = open("funcionarios.dat", "wb")
    pickle.dump(funcionarios, funcionariosArquivo)
    funcionariosArquivo.close()

def gravar_locacoes(locacoes):
    locacoesArquivo = open("locacoes.dat", "wb")
    pickle.dump(locacoes, locacoesArquivo)
    locacoesArquivo.close()