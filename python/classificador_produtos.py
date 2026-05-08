# Script de Análise de Estoque Logístico
# Objetivo: Classificar produtos e calcular necessidade de embalagens (caixas)
# Autor: Diego
estoque = [12, 45, 7, 18, 30, 55, 3, 24, 10, 11]
for quantidade in estoque:
    # Calcula a logística de embalagem (caixas de 5 unidades)
    caixas = quantidade // 5
    sobra = quantidade % 5
    # Define o status do produto com base na quantidade atual
    if quantidade < 10:
        print(f"Produto {quantidade}:  ESTOQUE CRITICO! ({caixas} caixas e {sobra} unidades)")   
    elif quantidade >= 10 and quantidade <20:
        print (f"Produto {quantidade}: Estoque baixo. ({caixas} caixas e {sobra} unidades)")
    else:
        print (f"Produto {quantidade}: Estoque suficiente. ({caixas} caixas e {sobra} unidades)")
    # Exibe o relatório consolidado para o setor de expedição