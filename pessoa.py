
class Pessoa:
    """Classe para Pessoa

    Atributes:
        nome: string
        rg: string
        endereco:string
        contato: string
    """
    nome = ""
    rg = ""
    endereco = "" 
    contato = ""
    
    # def __init__(self, nome, rg, endereco, contato):
    #     self.nome = nome
    #     self.rg = rg
    #     self.endereco = endereco
    #     self.contato = contato
        
    # def print_dados(self):
    #     print(self.nome)
    #     print(self.rg)
    #     print(self.endereco)
    #     print(self.contato)
    
    def get_nome(self):
        return self.nome
    
    def get_rg(self):
        return self.rg
    
    def get_endereco(self):
        return self.endereco
    
    def get_contato(self):
        return self.contato
    
    def set_nome(self, i):
        try:
            self.nome = i
        except Exception as e:
            print("erro: ", str(e))
            
    def set_rg(self, i):
        try:
            self.rg = i
        except Exception as e:
            print("erro: ", str(e))

    def set_endereco(self, i):
        try:
            self.endereco = i
        except Exception as e:
            print("erro: ", str(e))

    def set_contato(self, i):
        try:
            self.contato = i
        except Exception as e:
            print("erro: ", str(e))

