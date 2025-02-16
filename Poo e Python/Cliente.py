
# Criação de CLASSE
class Cliente:
    # Método CONSTRUTOR
    def __init__(self, n, tel):
        self.nome = n
        self.telefone = tel
    # MÉTODO

    def mostraDados(self):
        print(self.nome)
        print(self.telefone)


# Sintaxe de Métodos em Python:

# def nome_metodo(self,[parâmetros]): ** Adicionar parâmetros caso necessário
#     instruções = o que o método fará
#     {
#         em caso de parametros adicionados, esses devem ser inicializados / declarados
#         ex:
#         self.parametro_adicionado = nomeQualquer
#     }

#     return [valor] * ás vezes é preciso retornar algum valor
