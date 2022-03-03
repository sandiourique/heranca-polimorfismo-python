from modules.pessoa import Pessoa

class Aluno(Pessoa):
    """Classe do tipo Aluno

    Atributes:
        matricula: string
    """
    
    matricula = ""
    
    # def __init__(self, pessoa, matricula):        
    #     self.matricula = matricula
    
   
    def get_matricula(self):
        return self.matricula
    
           
    def set_matricula(self, i):
        try:
            self.matricula = i
        except Exception as e:
            print("erro: ", str(e))
            

