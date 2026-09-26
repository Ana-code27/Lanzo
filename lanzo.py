produtos = []           # Lista que armazena todos os produtos cadastrados.
numero_cliente = 1      # Número do próximo cliente. Começa em 1 e aumenta a cada venda registrada.
vendas = []             # Lista que armazena todas as vendas realizadas.


# Exibe o menu principal do sistema e retorna
# a opção escolhida pelo usuário.
def menu():
    print("*** LANZO ***")
    print("01. Cadastrar produto")
    print("02. Listar produtos")
    print("03. Registrar venda")
    print("04. Listar vendas")
    print("05. Ver total do caixa")
    print("06. Sair")

    while True:
        try:
            opcao = int(input("Digite uma opção: "))

            if opcao < 1 or opcao > 6:
                print("Opção inválida!")
            else:
                return opcao

        except ValueError:
            print("Opção inválida!")


# Exibe o menu pela primeira vez.
opcao = menu()


# O programa continua funcionando enquanto
# a opção escolhida for diferente de 6 (Sair).
while opcao != 6:

    # --------------------------------------------------
    # OPÇÃO 1 - CADASTRAR PRODUTO
    # --------------------------------------------------
    if opcao == 1:
        print("********************")
        print("CADASTRANDO PRODUTO")

        # Solicita o nome do produto.
        produto_nome = input("Digite o nome do produto: ").strip()

        while not produto_nome:
            print("Erro: o nome do produto não pode ser vazio")
            produto_nome = input("Digite o nome do produto: ").strip()
        # Solicita o preço do produto.
        # float() permite trabalhar com valores decimais.
        try:
            produto_uni = float(
                input("Digite o valor da unidade do produto: ")
            )

            if produto_uni <= 0:
                print("Valor inválido!")

            else:
                # Cria um dicionário contendo os dados do produto.
                produto_add = {
                    "produto": produto_nome,
                    "valor": produto_uni
                }

                # Adiciona o dicionário à lista de produtos.
                produtos.append(produto_add)

        except ValueError:
            print("Valor inválido!")

        # Exibe o menu novamente.
        opcao = menu()


    # --------------------------------------------------
    # OPÇÃO 2 - LISTAR PRODUTOS
    # --------------------------------------------------
    elif opcao == 2:
        print("********************")
        print("LISTA DE PRODUTOS")

        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto_add in produtos:
                print(
                    f"Produto: {produto_add['produto']}, "
                    f"Valor: R$ {produto_add['valor']:,.2f}"
                    .replace(",", "X")
                    .replace(".", ",")
                    .replace("X", ".")
                    )

        opcao = menu()


    # --------------------------------------------------
    # OPÇÃO 3 - REGISTRAR VENDA
    # --------------------------------------------------
    elif opcao == 3:
        print("********************")
        print("REGISTRANDO VENDA")

        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print(f"CLIENTE {numero_cliente}")

            pedido = input("Digite o produto desejado: ").strip()

            try:
                quantidade = int(input("Digite a quantidade: "))

                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero!")

                else:
                    encontrado = False

                    for produto_add in produtos:
                        if pedido == produto_add["produto"]:

                            total = produto_add["valor"] * quantidade

                            print(
                                f"Total: R$ {total:,.2f}"
                                .replace(",", "X")
                                .replace(".", ",")
                                .replace("X", ".")
                            )

                            encontrado = True

                            venda = {
                                "Cliente": numero_cliente,
                                "Total": total
                            }

                            vendas.append(venda)

                            numero_cliente += 1
                            
                            break

                    if not encontrado:
                        print("Produto não encontrado.")

            except ValueError:
                print("A quantidade deve ser um número inteiro.")

        opcao = menu()


    # --------------------------------------------------
    # OPÇÃO 4 - LISTAR VENDAS
    # --------------------------------------------------
    elif opcao == 4:
        print("********************")
        print("TODAS AS SUAS VENDAS")

        # Percorre todas as vendas registradas.
        for venda in vendas:
            print(
                f"Cliente: {venda['Cliente']}, "
                f"Total: {venda['Total']}"
            )

        # Volta para o menu.
        opcao = menu()


    # --------------------------------------------------
    # OPÇÃO 5 - VER TOTAL DO CAIXA
    # --------------------------------------------------
    elif opcao == 5:
        print("********************")
        print("TOTAL DO CAIXA")

        # Começa o acumulador do caixa em zero.
        vendas_total = 0

        # Percorre todas as vendas realizadas.
        for venda in vendas:

            # Soma o total de cada venda ao acumulador.
            vendas_total += venda["Total"]

        # Exibe a soma de todas as vendas.
        print(
            "Todas suas vendas somaram: R$ {}"
            .format(vendas_total)
        )

        # Volta para o menu.
        opcao = menu()


print("Sistema encerrado.")