roupas = {
    "Comuns": {                
        "Vestido": {
            "Estoque": 15,
            "Preco": 80
            # ID, DESCRICAO, TAMANHO, VALOR
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
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                                -|")
                print("|-        Todas as Roupas         -|")
                print("|-           e Fantasias          -|")
                print("|-                                -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                
                print()
                for key, value in roupas["Comuns"].items():
                    print(">", key, "- Estoque:", value["Estoque"])
                print()
                input("Aperte (ENTER) para continuar.")
                print()

            elif resp_roupas == "2":
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-  SubMódulo de ADD produtos -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("|-                            -|")
                print("|-     Em desenvolvimento     -|")
                print("|-                            -|")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
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


