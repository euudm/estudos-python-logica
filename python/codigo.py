vendas_brutas = [
    ["Celular", 1500, 2],    # Venda OK
    ["Notebook", 3500, 0],   # Erro: Quantidade zero
    ["Fone", -50, 1],        # Erro: Preço negativo
    ["Mouse", 80, 5],        # Venda OK
    ["Tablet", 1200, 1],     # Venda OK
    ["Teclado", 0, 2]        # Erro: Preço zero
]

for preco in vendas_brutas:
    produto = preco[0]
    valor = preco[1]
    quantidade = preco[2]
    if valor > 0 and quantidade >0:
        print (f"Venda de {produto} aprovada!")
    elif valor <= 0:
        print (f"Erro: {produto} está com preço inválido")
    elif quantidade <= 0:
        print (f"Erro: {produto} está sem estoque")
