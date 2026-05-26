def gerar_relatorio():
    nome_cliente = input("Nome do cliente: ")
    nome_produto = input("Nome do produto: ")
    quantidade = float (input("quantidade de produto: "))
    preco_unitario = float (input("Digite o preço unitario: "))

    subtotal = quantidade * preco_unitario
    imposto = subtotal * 0.05
    total_final = subtotal + imposto

    print(total_final)

    print("\n" + "="*50)
    print("{:^50}".format("RELATÓRIO DE VENDA"))
    print("="*50)
    print(f"CLIENTE: {nome_cliente.upper()}")
    print("-" * 50)
    
    # Aqui criamos o cabeçalho das colunas
    print(f"{'PRODUTO':<25} {'QTD':<5} {'TOTAL':>18}")
    
    # Aqui formatamos a linha do item (o :.2f garante os centavos)
    print(f"{nome_produto:<25} {quantidade:<5} R$ {total_final:>15.2f}")
    
    print("-" * 50)
    print(f"IMPOSTOS RECOLHIDOS (5%):      R$ {imposto:>15.2f}")
    print(f"VALOR TOTAL A PAGAR:           R$ {total_final:>15.2f}")
    print("="*50)
    print("{:^50}".format("Obrigado pela preferência!"))
    print("="*50)
gerar_relatorio()
