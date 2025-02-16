
# Criação de CLASSE
class Cliente2:
    # Método CONSTRUTOR
    def __init__(self, n, tel):
        self._nome = n
        self.telefone__ = tel
    # MÉTODO

    def get_telefone(self):
        return self._telefone
    

    def get_nome(self):
        return self._nome
    
    def set_telefone(self,tel):
        self.telefone__ = tel
        

    def mostraDados(self):
        print(self._nome)
        print(self.telefone__)
