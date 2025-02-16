# Em Python o comando While funciona de forma parecida com outras linguagens,

# O comando While será executado enquanto a condição for verdadeira.
# Em While a variavel deve ser declarada antes.

X = 1

while X <= 15:
    print(X)
    X = X+1

    # O X será mostrado em tela do 1 (seu valor atribuido na declaração)
    # ao numero 15(imposto na condição While)
print ('\n')

valor = float(input('Digite um valor: '))
soma  = 0
qtd   = 0 
media = 0

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1
    # Entrada de valores
    valor = float(input('Digite um valor: '))

media = soma / qtd
print('\n Total da soma: ', soma)
print('\n Quantidade de valores digitados: ',qtd)
print('\n Media dos valores: ',media)
