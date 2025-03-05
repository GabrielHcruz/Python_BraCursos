
# Como a classe Main não possui atributos.
# Utilizamos apenas a palavra reservada pass.
from Cliente import Cliente
# from (arquivo.py) import (classe ou *(todas as classes) em um arquivo)
from Conta import Conta

class Main:
    pass


print("Testando o projeto ")

# Para instanciar o objeto de uma classe para outra, devemos criar a referência da classe que será instanciada.
# A linha abaixo serve para trazer(importar) uma Classe.
# from é utilizada para indicar qual classe será importada,
# import é a referência de qual classe será utilizada para a criação de objetos em um arquivo à parte.

c1 = Cliente('João', "999-1234")
conta = Conta(c1.nome,23234,'R$ 0.0')

# Na linguagem Python, todo objeto criado possui um código de identificação composto por um número
# inteiro não negativo, conhecido como ID. Esse ID diferencia objeto e atributos deste objeto.


print(c1)
# print(c1), exibe o ID do objeto c1

c1.mostraDados()
# Aciona o método mostradados()

print (conta.titular,' Numero: ',conta.conta, 'Seu saldo: ',conta.saldo)
