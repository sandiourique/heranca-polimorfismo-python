from modules.pessoa import Pessoa

class Funcionario(Pessoa):
    """Classe do tipo Funcionario

    Atributes:
        salario: string
    """
    
    id = "" 
    cargo = ""
    
    # def __init__(self, salario):
    #     self.salario = salario
    
   
    def get_id(self):
        return self.id
    
    def get_cargo(self):
        return self.cargo
    
                
    def set_id(self, i):
        try:
            self.id = i
        except Exception as e:
            print("erro: ", str(e))


    def set_cargo(self, i):
        try:
            self.cargo = i
        except Exception as e:
            print("erro: ", str(e))
