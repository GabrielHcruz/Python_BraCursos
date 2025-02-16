
def LerNotas():
    n = float(input('Digite a nota: '))
    return n


def Resultado(n1, n2):
    media = (n1 + n2) / 2

    print('\nNota 1: ', n1)
    print('Nota 2: ', n2)
    print('Media: ', media)

    if media >= 6:
        print('\nAprovado!')
    else:
        print('\nReprovado')


A = LerNotas()
B = LerNotas()

Resultado(A, B)

# A função Resultado possui parametros (n1 e n2),
# Quando chamamos a função Resultado acima, as variaveis A e B são colocadas como
# parametros e assumem as posições (n1 e n2) *respectivamente*Isso é importante
