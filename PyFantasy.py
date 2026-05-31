roupas = {
    "Comuns": {                
        1: {
            "Nome": "Vestido",
            "Valor": 80,
            "Descricao": "Vestido vermelho com listras.",
            "Tamanho": "G"
        },
    },
    "Fantasias": {}
}

resp = ""
while resp != "0":
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("|-                                        -|")
    print("|-            Fantasy Wardrobe            -|")
    print("|-                                        -|")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("|-          1 - Roupas e Fantasias        -|")
    print("|-          2 - Clientes                  -|")
    print("|-          3 - Funcionários              -|")
    print("|-          4 - Gerenciar Locação         -|")
    print("|-          0 - Sair do sistema           -|")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    resp = input("Digite o número do módulo que quer acessar: ")

    if resp == "1":

        resp_roupas = ""
        while resp_roupas != "0":
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-                                      -|")
            print("|-            Módulo de Roupas          -|")
            print("|-               e Fantasias            -|")
            print("|-                                      -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("|-     1 - Listar todos os produtos     -|")
            print("|-     2 - Adicionar produtos           -|")
            print("|-     3 - Remover produtos             -|")
            print("|-     0 - Voltar                       -|")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

            resp_roupas = input("Digite o número do submódulo que quer acessar: ")

            if resp_roupas == "1":
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                -|")
                print("|-        Todas as Roupas         -|")
                print("|-           e Fantasias          -|")
                print("|-                                -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                
                for key, value in roupas["Comuns"].items():
                    print("> ID:", key,"-", value["Nome"], "- Tamanho:", value["Tamanho"], "- Valor: R$", value["Valor"])
                    
                print()
                input("Aperte (ENTER) para continuar.")
                print()

            elif resp_roupas == "2":
                print()
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-      Adicionar produto     -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                
                nome_produto = input("Digite o nome do produto: ")
                
                while True:
                    try:
                        valor_produto = float(input("Digite o valor do produto: "))
                    except ValueError:
                        print()
                        print("Erro: Digite um número válido.")
                        continue

                    if valor_produto < 0:
                        print()
                        print("Erro: O valor do produto não pode ser negativo.")
                        continue

                    break
                
                desc_produto = input("Digite a descrição do produto: ")
                print("Padrão de tamanhos: (PP, P, M, G, GG, XG)")
                tam_produto = input("Digite o tamanho do produto: ")
                
                while tam_produto.lower() not in ["pp", "p", "m", "g", "gg", "xg"]:
                    print()
                    print("Tamanho inválido. Tente novamente! Tamanhos válidos: (PP, P, M, G, GG, XG)")
                    tam_produto = input("Digite o tamanho do produto: ")
                    
                id_produto = len(roupas["Comuns"]) + 1
                roupas["Comuns"][id_produto] = {
                    "Nome": nome_produto,
                    "Valor": valor_produto,
                    "Descricao": desc_produto,
                    "Tamanho": tam_produto
                }
                print("(ID: %d) Produto adicionado com sucesso!"%(id_produto))

                print()
                input("Aperte (ENTER) para continuar.")
                print()
            elif resp_roupas == "3":
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-     SubMódulo de Remover   -|")
                print("|-          produtos          -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-     Em desenvolvimento     -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print()
                input("Aperte (ENTER) para continuar.")
                print()

        

    
    elif resp == "2":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-                            -|")
        print("|-     Módulo de Clientes     -|")
        print("|-                            -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-                            -|")
        print("|-     Em desenvolvimento     -|")
        print("|-                            -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        input("Aperte (ENTER) para continuar.")
        print()

    elif resp == "3":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-                            -|")
        print("|-    Módulo de Funcionários  -|")
        print("|-                            -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-                            -|")
        print("|-     Em desenvolvimento     -|")
        print("|-                            -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        input("Aperte (ENTER) para continuar.")
        print()

    elif resp == "4":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-                            -|")
        print("|-    Módulo de Locações      -|")
        print("|-                            -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("|-                            -|")
        print("|-     Em desenvolvimento     -|")
        print("|-                            -|")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print()
        input("Aperte (ENTER) para continuar.")
        print()


