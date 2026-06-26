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
            },
            2: {
                "Nome": "Vestido de Gala",
                "Valor": 150,
                "Descricao": "Vestido longo vermelho com brilho.",
                "Tamanho": "M",
                "Categoria": "Comum",
                "Ativo": True
            },
            3: {
                "Nome": "Fantasia de Pirata",
                "Valor": 95,
                "Descricao": "Conjunto completo com chapéu e tapa-olho.",
                "Tamanho": "P",
                "Categoria": "Fantasia",
                "Ativo": True
            },
            4: {
                "Nome": "Fantasia de Super-Herói",
                "Valor": 110,
                "Descricao": "Macacão com capa e máscara.",
                "Tamanho": "PP",
                "Categoria": "Fantasia",
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
                "DataNascimento": "15/12/2000",
                "Ativo": True
            },
            2: {
                "Nome": "Maria Joaquina",
                "CPF": "52998224725",
                "Telefone": "(84) 98765-4321",
                "Email": "maria.joaquina@gmail.com",
                "Endereco": "Av. Engenheiro Roberto Freire, 1500, Capim Macio, Natal - RN, CEP 59082-100",
                "DataNascimento": "22/03/1995",
                "Ativo": True
            },
            3: {
                "Nome": "João Pedro Costa",
                "CPF": "11144477735",
                "Telefone": "(84) 91234-5678",
                "Email": "joaopedro.costa@hotmail.com",
                "Endereco": "Rua Apodi, 320, Tirol, Natal - RN, CEP 59020-130",
                "DataNascimento": "08/09/1988",
                "Ativo": True
            },
            4: {
                "Nome": "Ana Beatriz Lima",
                "CPF": "39053344705",
                "Telefone": "(84) 99876-5432",
                "Email": "anabeatriz.lima@outlook.com",
                "Endereco": "Rua Potengi, 87, Petrópolis, Natal - RN, CEP 59020-160",
                "DataNascimento": "30/06/1992",
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
                "DataNascimento": "05/06/1997",
                "Ativo": True
            },
            2: {
                "Nome": "Carla Fernanda Souza",
                "CPF": "93541134780",
                "Telefone": "(84) 98123-4567",
                "Email": "carla.souza@fantasywardrobe.com",
                "Endereco": "Av. Hermes da Fonseca, 980, Tirol, Natal - RN, CEP 59020-650",
                "DataNascimento": "12/02/1990",
                "Ativo": True
            },
            3: {
                "Nome": "Ricardo Alves Pereira",
                "CPF": "15350946056",
                "Telefone": "(84) 97654-3210",
                "Email": "ricardo.pereira@fantasywardrobe.com",
                "Endereco": "Rua Mossoró, 412, Petrópolis, Natal - RN, CEP 59020-540",
                "DataNascimento": "27/11/1985",
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
            },
            2: {
                "ID_Cliente": 2,
                "ID_Produto": 2,
                "CheckIn": "10/06/2026",
                "CheckOut": "15/06/2026",
                "Ativo": True
            },
            3: {
                "ID_Cliente": 3,
                "ID_Produto": 3,
                "CheckIn": "01/04/2026",
                "CheckOut": "08/04/2026",
                "Ativo": False
            },
            4: {
                "ID_Cliente": 4,
                "ID_Produto": 4,
                "CheckIn": "20/07/2026",
                "CheckOut": "27/07/2026",
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