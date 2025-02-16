# Diferente da maioria das linguagens, uma variável em Python não tem um tipo fixo,
# apenas o tipo do conteúdo.
#  Diferente de outras linguagens o Python não exige que as variáveis sejam declaradas
# no inicio do codigo, ou que tenham um 'tipo de dado' atribuído
# EX:

nome = 'Carlos'
idade = 30
salario = 1500.0

nome2 = 'Marcos'
idade2 = 25
salario2 = 2500.0

# Observe que a variavel nome = 'Carlos' abriga um dado do tipo Character
# mas não possuí essa declarção em código. Isso acontece porque o Python já
# reconhece naturalmente os tipos de dados.

# PS... não considero uma prática saudável

# Concatenação

print('Nome: ', nome, 'Salario: ', salario, 'idade: ', idade)

# ou

print('\nNome: ' + nome2 + '\nSalario: ' +
      str(salario2) + '\nidade: ' + str(idade2))

# colocamos str(nome variável) antes das variáveis que não são do tipo String

# Formatação de Strings

#       \t   Insere tabulação horizontal.
#       \v   Insere tabulação vertical.
#       \n   Insere uma quebra de linha.
#       \r   Equivalente ao efeito da tecla Enter.
#       \’   Aspas simples.
#       \”   Aspas duplas.
#       \\   Insere uma barra invertida (backslash).
#       \a   Chamado de asc bell ou beep do sistema. Se houver suporte, aciona um bipe.
#       \b   Aciona o backspace, ou seja, apaga o caractere anterior.
#       \f   Insere uma quebra de página.
#       \u   Insere um caractere unicode. Deve acompanhar um código com 4 números.
