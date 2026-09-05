produtos = []
numero_cliente = 1

def menu():
    print("*** LANZO ***")
    print("01. Cadastrar produto")
    print("02. Listar produtos")
    print("03. Registrar venda")
    print("04. Listar vendas")
    print("05. Ver total do caixa")
    print("06. Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

opcao = menu()

while opcao != 6:
    if opcao == 1:
        print("********************")
        print("CADASTRANDO PRODUTO")
        produto = input("Digite o nome do produto: ")
        produto_uni = float(input("Digite o valor da unidade do produto: "))

        produto_add = {"produto": produto, "valor": produto_uni}
        produtos.append(produto_add)
        opcao = menu()

    elif opcao == 2:
        print("********************")
        print("LISTA DE PRODUTOS")
        for produto_add in produtos:
            print(f"Produto: {produto_add['produto']}, Valor: {produto_add['valor']}")
        opcao = menu()

    elif opcao == 3:
        print("********************")
        print("REGISTRANDO VENDA")
        print(f"CLIENTE {numero_cliente}")
        pedido = input("Digite o produto desejado: ")
        quantidade = float(input("Digite a quantidade: "))

        for produto_add in produtos:
            if pedido == produto_add["produto"]:
             total = produto_add["valor"] * quantidade
             print("Total: R$ {}" .format(total))
        numero_cliente += 1
        opcao = menu()