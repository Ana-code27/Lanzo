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
        except:
            print("Opção invalida!")


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
        produto = input("Digite o nome do produto: ")

        # Solicita o preço do produto.
        # float() permite trabalhar com valores decimais.
        try:
            produto_uni = float(
            input("Digite o valor da unidade do produto: "))

            if produto_uni <= 0:
                print("Valor invalido!")
            else:
             # Cria um dicionário contendo os dados do produto.
             produto_add = {
                 "produto": produto,
                 "valor": produto_uni
                 }
             # Adiciona o dicionário à lista de produtos.
             produtos.append(produto_add)

        except ValueError:
            print("Valor invalido!")
        
        # Exibe o menu novamente.
        opcao = menu()


    # --------------------------------------------------
    # OPÇÃO 2 - LISTAR PRODUTOS
    # --------------------------------------------------
    elif opcao == 2:
        print("********************")
        print("LISTA DE PRODUTOS")

        # Percorre todos os produtos cadastrados.
        for produto_add in produtos:
            print(
                f"Produto: {produto_add['produto']}, "
                f"Valor: {produto_add['valor']}"
            )

        # Volta para o menu.
        opcao = menu()

    # --------------------------------------------------
    # OPÇÃO 3 - REGISTRAR VENDA
    # --------------------------------------------------
    elif opcao == 3:
        print("********************")
        print("REGISTRANDO VENDA")

        # Mostra automaticamente o número do cliente.
        print(f"CLIENTE {numero_cliente}")

        # Solicita o produto que será vendido.
        pedido = input("Digite o produto desejado: ")

        # Solicita a quantidade.
        quantidade = int(input("Digite a quantidade: "))

        if quantidade <= 0:
            print("Quantidade invalida!")

        else:
            # Começa como False porque nenhum produto foi encontrado ainda.
            encontrado = False

            # Percorre os produtos cadastrados para encontrar
            # aquele que corresponde ao pedido do cliente.
            for produto_add in produtos:

                if pedido == produto_add["produto"]:
                    # Calcula o valor total da venda:
                    # preço do produto × quantidade.
                    total = produto_add["valor"] * quantidade

                    # Exibe o valor total da venda.
                    print("Total: R$ {}".format(total))

                    # Indica que o produto foi encontrado.
                    encontrado = True
                

            # Verifica se o produto não foi encontrado.
            if not encontrado:
                print("Produto não encontrado")

            # Só registra a venda se o produto tiver sido encontrado.
            if encontrado:

                # Cria um dicionário com os dados da venda.
                venda = {
                    "Cliente": numero_cliente,
                    "Total": total
                }

                # Adiciona a venda à lista de vendas.
                vendas.append(venda)

                # Aumenta o número do cliente para a próxima venda.
                numero_cliente += 1

        # Volta para o menu.
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