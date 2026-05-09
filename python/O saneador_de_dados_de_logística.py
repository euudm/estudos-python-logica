pedidos = [101, 0, 105, -1, 108, 0, 112, 115, -5, 120]

#Neste exercício, aprendi dois conceitos:
#MÉTODO .append()
#FUNÇÃO len()
#CONCEITO APLICADO: 
#Usei o 'for' para percorrer os pedidos, o 'if' para validar, o '.append()' para organizar os resultados e o 'len()' para o resumo final.


pedidos_validos = []
pedidos_invalidos = []

for pedido in pedidos:
    if pedido > 0:
        pedidos_validos.append(pedido)
    else:
        pedidos_invalidos.append(pedido)
print("Análise de Pedidos Logísticos")
print("-----------------------------")  
print(f"Total de Pedidos: {len(pedidos)}")  
print("Pedidos Válidos:", pedidos_validos)
print("Pedidos Inválidos:", pedidos_invalidos)