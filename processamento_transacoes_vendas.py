#lista de vendas do e-commerce do cliente
vendas_dia = [
    ["Mouse", 50, 2],
    ["Teclado", 150, 1],
    ["Monitor", 900, 2],
    ["Fone", 100, 3]
]
faturamento_total = 0

#cliente queria o valor total de cada venda
#faturamento total do dia, somando todas as vendas
#e colocar que se a venda for maior que 1000, a meta foi batida, senão, a meta não foi batida

#calculando toda de cada venda
for venda in vendas_dia:
    produto = venda[0]
    preco = venda [1]
    quantidade = venda [2]
    valor_desta_venda = preco * quantidade
    print (f"Venda de {produto} no valor de R${valor_desta_venda:.2f}")
#somando o faturametno total do dia
    faturamento_total = faturamento_total + valor_desta_venda
print (f"O faturamento total do dia foi de R${faturamento_total:.2f}")
#colocando se a meta foi atigica ou não
if faturamento_total > 1000:
    print ("Meta batida!")
else :
    print ("Meta não batida!")
