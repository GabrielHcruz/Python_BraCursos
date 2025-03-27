
# Existem três métodos principais de formatação de strings em Python:
#     f-strings
#     str.format()
#     formatação com % .

# Entre elas a mais poderosa e versátil é o f-strings.

nome = "Maria"
idade = 30


# Pondo em prática

#     F-Strings
mensagem = f"Olá, meu nome é {nome} e tenho {idade} anos."

#     .format
mensagem1 = "Olá, meu nome é {} e tenho {} anos." .format(nome, idade)

#     %
mensagem2 = "Olá, meu nome é %s e tenho %d anos." % (nome, idade)

print(mensagem)

# Para formatação numérica

preco = 128.456

# f-string
formtNumerica = f"Preço: R$ {preco:.2f}"

# str.format()
formtNumerica2 = "Preço: R$ {:.2f}".format(preco)

# %
formtNumerica3 = "Preço: R$ %.2f" % preco

print(formtNumerica)

# Bônus:

# Alinhar texto:

#     nome = "Python"
#     print(f"{nome:<10} é incrível!")  -- Alinha à esquerda

#     print(f"{nome:>10} é incrível!")  -- Alinha à direita

#     print(f"{nome:^10} é incrível!")  -- Centraliza


# Porcentagem:

#     taxa = 0.15
#     print(f"A taxa é {taxa:.1%}")

# Números grandes com separadores de milhar:

#     valor = 1000000
#     print (f"Valor: R${valor:,.2f}")
