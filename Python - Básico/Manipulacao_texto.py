
# Por meio da linguagem Python, podemos manipular dados em um arquivo texto, mostrando as operações básicas de leitura e escrita.

# Esse arquivo texto é conhecido como arquivo sequencial, porque a leitura tem de ser feita de forma sequencial, do início ao fim do arquivo.

# Para trabalharmos com arquivos texto na linguagem Python utilizamos funções.

arquivo = open('Manual.txt', 'w')
# arquivo é uma variavel para executar a função open()
# A função open() abre ou cria um arquivo, o nome do arquivo é colocado dentro dos
# parenteses com aspas simples 'Manual.txt'
# Se já existir um arquivo com esse nome todo o conteúdo dele será reescrito
# o 'w' no final indica q o arquivo esta sendo aberto para escrita w = write


# arquivo.write serve para escrever no documento
arquivo.write('Manual Sobre os Arquivos deste repositório')
arquivo.write('\nO nome de cada arquivo envolve seu tema')

# A função close() é muito importante para encerrar o arquivo após sua utilização.
# É preciso sempre lembrar de fechar um documento
arquivo.close()


# A função read() realiza a leitura
# de todo conteúdo do arquivo.
# Sua sintaxe é:

leitura = open('Manual.txt', 'r')

print(leitura.read())

leitura.close()

# Ao utilizar a função read(), o nome do arquivo deve ser:

# 1) Uma string com o caminho completo (por exemplo, C Documentos teste txt)
# ou
# 2) O caminho em relação ao diretório atual (nomes txt do arquivo que se deseja abrir).
