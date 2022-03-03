from modules.pessoa import Pessoa
from modules.aluno import Aluno

class AlunoPortugues(Aluno):
    """Classe do tipo Aluno Português

    Atributes:
        nota: string
    """
    
    nota = ""
    
    # def __init__(self, nota):
    #     self.nota = nota
    
   
    def get_nota(self):
        return self.nota
    
           
    def set_nota(self, i):
        try:
            self.nota = i
        except Exception as e:
            print("erro: ", str(e))