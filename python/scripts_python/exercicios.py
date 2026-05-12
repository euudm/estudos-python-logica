nome = "joão paulo lira"
email = "emailfalsodolira@gmail.com"



nome_1 = nome [0:5] #utilizei o 0:5 para pegar os 5 primeiros caracteres da string, ou seja, "joão " (incluindo o espaço).
nome_1 = nome_1.capitalize() # aqui usei o capitalize() para deixar a primeira letra maiúscula e as demais minúsculas, resultando em "João ".

posicao = email.find("@") # aqui usei o find() para encontrar a posição do caractere "@" na string do email, pra depois pegar so ó domninio do email.

email_1 = email [posicao+1:] # usei o slicing para pegar a parte do email que vem depois do "@" (posicao+1 para não incluir o "@"), resultando em "gmail.com".

print(f"o usario {nome_1}foi cadastadrado com o email:{email_1}")



