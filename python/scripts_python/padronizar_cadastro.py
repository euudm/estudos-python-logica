cliente_bruto = "  diEgo silvA_Logistica-2026  "

# Passo 1: Remover espaços em branco no início e no final
cliente_limpo = cliente_bruto.strip()

# Passo 2: Converter para letras minúsculas
cliente_limpo = cliente_limpo.title()

# Passo 3: Substituir caracteres indesejados (exemplo: substituir "_" por " ")
cliente_limpo = cliente_limpo.replace("_"," ",) 
cliente_limpo = cliente_limpo.replace("-", " - Ano ",)
#adicionando o nome limpor do cliente a uma variável para criar um apelido e um ano
apelido = cliente_limpo[0:6]
ano = 2026
#resultado final
print(f"Cliente: {cliente_limpo}, - Apelido: {apelido}, - Ano: {ano:.1f}")







