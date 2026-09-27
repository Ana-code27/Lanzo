produtos = []           # Produtos cadastrados.
numero_cliente = 1      # Número do próximo cliente.
vendas = []             # Vendas realizadas.


# Exibe o menu principal e retorna a opção escolhida.
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


# Mantém o sistema em funcionamento até a opção 6.
while opcao != 6:

    # --------------------------------------------------
    # OPÇÃO 1 - CADASTRAR PRODUTO
    # --------------------------------------------------
    if opcao == 1:
        print("********************")
        print("CADASTRANDO PRODUTO")

        produto_nome = input("Digite o nome do produto: ").strip()

        # Impede o cadastro de produtos sem nome.
        while not produto_nome:
            print("Erro: o nome do produto não pode ser vazio")
            produto_nome = input("Digite o nome do produto: ").strip()

        try:
            produto_uni = float(
                input("Digite o valor da unidade do produto: ")
            )

            if produto_uni <= 0:
                print("Valor inválido!")

            else:
                produto_add = {
                    "produto": produto_nome,
                    "valor": produto_uni
                }

                produtos.append(produto_add)

        except ValueError:
            print("Valor inválido!")

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

                            # Só avança após uma venda válida.
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
        print("TODAS AS VENDAS")

        if not vendas:
            print("Nenhuma venda cadastrada.")
        else:
            for venda in vendas:
                print(
                    f"Cliente: {venda['Cliente']}, "
                    f"Total: R$ {venda['Total']:,.2f}"
                    .replace(",", "X")
                    .replace(".", ",")
                    .replace("X", ".")
                    )

        opcao = menu()


    # --------------------------------------------------
    # OPÇÃO 5 - VER TOTAL DO CAIXA
    # --------------------------------------------------
    elif opcao == 5:
        print("********************")
        print("TOTAL DO CAIXA")

        if not vendas:
            print("Nenhuma venda cadastrada.")
        else:

            vendas_total = 0

            # Soma todas as vendas realizadas.
            for venda in vendas:
                vendas_total += venda["Total"]

            print(f"Todas suas vendas somaram: R$ {vendas_total:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
            )

        opcao = menu()


print("Sistema encerrado.")