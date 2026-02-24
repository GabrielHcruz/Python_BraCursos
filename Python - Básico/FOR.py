

for X in range (10):
    print('X: ',X)

# No exemplo acima, a variável X é inicialmente ajustada para 0 (valor padrão).

# Uma vez que X é menor do que 10 (condição), o comando print é executado.

# Essa condição é adicionada com o comando range(intervalo).

# A variável X é incrementada em 1 (incremento padrão)

# para alterar os valores de X, deve ser feita uma alteração dentro de range
# EX:
print('\n')

for Y in range(5, 15):
    print('Y: ' +str(Y))
    # +str(Y) = é uma forma de exibir informações, não muito diferente das aspas, seu uso aqui dispensa a necessidade da vírgula. ex: print('Y:' , Y)
    # +str(Y) = usado apenas em variaveis q NÃO SÃO Strings.
    # Nesse caso Y começa em 5 e vai até 14

print('\n')

    # Também é possivel utilizar decremento no contador, dentro do comando range
    # ex:
for A in range(10,0, -1):
    print(A)

# Naturalmente podemos somar de 2 em 2, subtrair de 3 em 3 e assim por diante
# ex:
print('\n')
for B in range(0,10, +2):
    print(B)
    
