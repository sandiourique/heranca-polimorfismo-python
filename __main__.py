"""
- Crie uma classe pessoa (nome, rg, endereco, contato)
- Crie uma classe funcionário (id, cargo) que herde de pessoa
- Crie uma classe aluno (matricula) que herde de pessoa
- Crie uma classe aluno de potugues (nota) que herde de aluno
- Crie uma classe aluno de matematica (nota) que herde de aluno
- Crie getters, setters, construtores e destrutores conforme necessário
- instancie 5 objetos de cada classe e apresente todos os dados de cadaum

"""

from modules.pessoa import Pessoa
from modules.aluno import Aluno
from modules.funcionario import Funcionario
from modules.alunoPortugues import AlunoPortugues
from modules.alunoMatematica import AlunoMatematica


if __name__ == "__main__":
    
    #Criando uma instância da classe Pessoa através do método construtor da classe
    print("----------------------------------------------------------------")
    print("Grupo de pessoas")
    print("----------------------------------------------------------------")
    pessoa1 = Pessoa()
    pessoa1.set_nome("Enzo")
    pessoa1.set_rg("5656565")
    pessoa1.set_endereco("Rua X")
    pessoa1.set_contato("5599999999")
    # pessoa1.print_dados()
    print(f" Nome: {pessoa1.get_nome()}, \n RG: {pessoa1.get_rg()}, \n Enderco: {pessoa1.get_endereco()}, \n Contato: {pessoa1.get_contato()} \n")

  
    pessoa2 = Pessoa()
    pessoa2.set_nome("Maria")
    pessoa2.set_rg("123456")
    pessoa2.set_endereco("Rua A")
    pessoa2.set_contato("5599999997")
    print(f" Nome: {pessoa2.get_nome()}, \n RG: {pessoa2.get_rg()}, \n Enderco: {pessoa2.get_endereco()}, \n Contato: {pessoa2.get_contato()} \n")
   
    pessoa3 = Pessoa()
    pessoa3.set_nome("Joao")
    pessoa3.set_rg("789456")
    pessoa3.set_endereco("Rua B")
    pessoa3.set_contato("5599999996")
    print(f" Nome: {pessoa3.get_nome()}, \n RG: {pessoa3.get_rg()}, \n Enderco: {pessoa3.get_endereco()}, \n Contato: {pessoa3.get_contato()} \n")
        
    pessoa4 = Pessoa()
    pessoa4.set_nome("Eros")
    pessoa4.set_rg("4567881")
    pessoa4.set_endereco("Rua C")
    pessoa4.set_contato("5599999995")
    print(f" Nome: {pessoa4.get_nome()}, \n RG: {pessoa4.get_rg()}, \n Enderco: {pessoa4.get_endereco()}, \n Contato: {pessoa4.get_contato()} \n")
    
    pessoa5 = Pessoa()
    pessoa5.set_nome("Sophia")
    pessoa5.set_rg("456124")
    pessoa5.set_endereco("Rua D")
    pessoa5.set_contato("5599999995")
    print(f" Nome: {pessoa5.get_nome()}, \n RG: {pessoa5.get_rg()}, \n Enderco: {pessoa5.get_endereco()}, \n Contato: {pessoa5.get_contato()} \n")
     
    # #Criando uma instância da classe Aluno através do método construtor da classe pai (Pessoa)
    print("----------------------------------------------------------------")
    print("Grupo de Alunos")
    print("----------------------------------------------------------------")
    aluno1 = Aluno()
    aluno1.set_nome("Laila")
    aluno1.set_rg("11572")
    aluno1.set_endereco("Rua E")
    aluno1.set_contato("5599999911")
    aluno1.set_matricula("29/11/2021")
    print(f" Nome: {aluno1.get_nome()},\n RG: {aluno1.get_rg()}, \n Endereco: {aluno1.get_endereco()}, \n Contato: {aluno1.get_contato()}, \n Matricula: {aluno1.get_matricula()} \n")

    aluno2 = Aluno()
    aluno2.set_nome("Tatiana")
    aluno2.set_rg("782512")
    aluno2.set_endereco("Rua F")
    aluno2.set_contato("5599999922")
    aluno2.set_matricula("10/11/2021")
    print(f" Nome: {aluno2.get_nome()},\n RG: {aluno2.get_rg()}, \n Endereco: {aluno2.get_endereco()}, \n Contato: {aluno2.get_contato()}, \n Matricula: {aluno2.get_matricula()} \n")


    aluno3 = Aluno()
    aluno3.set_nome("Tarsso")
    aluno3.set_rg("563356")
    aluno3.set_endereco("Rua E")
    aluno3.set_contato("5599999933")
    aluno3.set_matricula("10/10/2020")
    print(f" Nome: {aluno3.get_nome()},\n RG: {aluno3.get_rg()}, \n Endereco: {aluno3.get_endereco()}, \n Contato: {aluno3.get_contato()}, \n Matricula: {aluno3.get_matricula()}\n")

    aluno4 = Aluno()
    aluno4.set_nome("Sophia R")
    aluno4.set_rg("852258")
    aluno4.set_endereco("Rua G")
    aluno4.set_contato("5599999944")
    aluno4.set_matricula("01/11/2021")
    print(f" Nome: {aluno4.get_nome()},\n RG: {aluno4.get_rg()}, \n Endereco: {aluno4.get_endereco()}, \n Contato: {aluno4.get_contato()}, \n Matricula: {aluno4.get_matricula()} \n")

    aluno5 = Aluno()
    aluno5.set_nome("Lara Maria")
    aluno5.set_rg("965874")
    aluno5.set_endereco("Rua H")
    aluno5.set_contato("5599999955")
    aluno5.set_matricula("01/09/2021")
    print(f" Nome: {aluno5.get_nome()}, \n RG: {aluno5.get_rg()}, \n Endereco: {aluno5.get_endereco()}, \n Contato: {aluno5.get_contato()}, \n Matricula: {aluno5.get_matricula()} \n")

    #Criando uma instância da classe Funcionário através do método construtor da classe pai (Pessoa)
    print("----------------------------------------------------------------")
    print("Grupo de Funcionários")
    print("----------------------------------------------------------------")
    funcionario1 = Funcionario()
    funcionario1.set_nome("Lara Maria")
    funcionario1.set_rg("965874")
    funcionario1.set_endereco("Rua H")
    funcionario1.set_contato("5599999955")
    funcionario1.set_id("01")
    funcionario1.set_cargo("Analista de Dados")
    print(f" Nome: {funcionario1.get_nome()},\n RG: {funcionario1.get_rg()}, \n Endereco: {funcionario1.get_endereco()}, \n Contato: {funcionario1.get_contato()}, \n ID: {funcionario1.get_id()}, \n Cargo: {funcionario1.get_cargo()} \n")

    funcionario2 = Funcionario()
    funcionario2.set_nome("João")
    funcionario2.set_rg("22543265")
    funcionario2.set_endereco("Rua Manaus")
    funcionario2.set_contato("5599992222")
    funcionario2.set_id("02")
    funcionario2.set_cargo("Advogado")
    print(f" Nome: {funcionario2.get_nome()},\n RG: {funcionario2.get_rg()}, \n Endereco: {funcionario2.get_endereco()}, \n Contato: {funcionario2.get_contato()}, \n ID: {funcionario2.get_id()}, \n Cargo: {funcionario1.get_cargo()} \n")

    funcionario3 = Funcionario()
    funcionario3.set_nome("João")
    funcionario3.set_rg("33543365")
    funcionario3.set_endereco("Rua Manaus")
    funcionario3.set_contato("5599993333")
    funcionario3.set_id("03")
    funcionario3.set_cargo("Advogado")
    print(f" Nome: {funcionario3.get_nome()},\n RG: {funcionario3.get_rg()}, \n Endereco: {funcionario3.get_endereco()}, \n Contato: {funcionario3.get_contato()}, \n ID: {funcionario3.get_id()}, \n Cargo: {funcionario1.get_cargo()} \n")
 
    funcionario4 = Funcionario()
    funcionario4.set_nome("Alessandra")
    funcionario4.set_rg("4445556")
    funcionario4.set_endereco("Rua Ouro Verde")
    funcionario4.set_contato("5599994444")
    funcionario4.set_id("04")
    funcionario4.set_cargo("Psicologa")
    print(f" Nome: {funcionario4.get_nome()},\n RG: {funcionario4.get_rg()}, \n Endereco: {funcionario4.get_endereco()}, \n Contato: {funcionario4.get_contato()}, \n ID: {funcionario4.get_id()}, \n Cargo: {funcionario1.get_cargo()} \n")
  
    funcionario5 = Funcionario()
    funcionario5.set_nome("Ana")
    funcionario5.set_rg("55545565")
    funcionario5.set_endereco("Rua Ouro Verde")
    funcionario5.set_contato("5599995555")
    funcionario5.set_id("05")
    funcionario5.set_cargo("Advogado")
    print(f" Nome: {funcionario5.get_nome()},\n RG: {funcionario5.get_rg()},\n Endereco: {funcionario5.get_endereco()}, \n Contato: {funcionario5.get_contato()}, \n ID: {funcionario5.get_id()}, \n Cargo: {funcionario5.get_cargo()} \n")
   
    #Criando uma instância da classe AlunoPortugues através do método construtor da classe pai (Aluno)
    print("----------------------------------------------------------------")
    print("Grupo de Alunos de Português")
    print("----------------------------------------------------------------")
    
    alunoPortugues1 = AlunoPortugues()
    alunoPortugues1.set_nome("Glen")
    alunoPortugues1.set_rg("12456789")
    alunoPortugues1.set_endereco("Rua E")
    alunoPortugues1.set_contato("5591234445")
    alunoPortugues1.set_matricula("01/02/2021")
    alunoPortugues1.set_nota("6.5")
    print(f" Nome: {alunoPortugues1.get_nome()},\n RG: {alunoPortugues1.get_rg()}, \n Endereco: {alunoPortugues1.get_endereco()}, \n Contato: {alunoPortugues1.get_contato()}, \n Matricula: {alunoPortugues1.get_matricula()}, \n Nota: {alunoPortugues1.get_nota()} \n")

    alunoPortugues2 = AlunoPortugues()
    alunoPortugues2.set_nome("Rosa")
    alunoPortugues2.set_rg("226446789")
    alunoPortugues2.set_endereco("Rua J")
    alunoPortugues2.set_contato("5592235545")
    alunoPortugues2.set_matricula("02/02/2021")
    alunoPortugues2.set_nota("9.5")
    print(f" Nome: {alunoPortugues2.get_nome()}, \n RG: {alunoPortugues2.get_rg()}, \n Endereco {alunoPortugues2.get_endereco()}, \n Contato: {alunoPortugues2.get_contato()}, \n Matricula: {alunoPortugues2.get_matricula()}, \n Nota: {alunoPortugues2.get_nota()} \n")


    alunoPortugues3 = AlunoPortugues()
    alunoPortugues3.set_nome("Meredith")
    alunoPortugues3.set_rg("3246546487")
    alunoPortugues3.set_endereco("Rua I")
    alunoPortugues3.set_contato("5593254654")
    alunoPortugues3.set_matricula("03/02/2021")
    alunoPortugues3.set_nota("8.0")
    print(f" Nome: {alunoPortugues3.get_nome()}, \n RG: {alunoPortugues3.get_rg()}, \n Endereco: {alunoPortugues3.get_endereco()},\n Contato: {alunoPortugues3.get_contato()},  \n Matricula: {alunoPortugues3.get_matricula()}, \n Nota: {alunoPortugues3.get_nota()} \n")

    alunoPortugues4 = AlunoPortugues()
    alunoPortugues4.set_nome("Lorena")
    alunoPortugues4.set_rg("45671123")
    alunoPortugues4.set_endereco("Rua E")
    alunoPortugues4.set_contato("559565687")
    alunoPortugues4.set_matricula("01/02/2021")
    alunoPortugues4.set_nota("9.5")
    print(f" Nome: {alunoPortugues4.get_nome()}, \n RG: {alunoPortugues4.get_rg()}, \n Endereco: {alunoPortugues4.get_endereco()}, \n Contato: {alunoPortugues4.get_contato()}, \n Matricula: {alunoPortugues4.get_matricula()},\n Nota: {alunoPortugues4.get_nota()} \n")

    alunoPortugues5 = AlunoPortugues()
    alunoPortugues5.set_nome("Fabiano")
    alunoPortugues5.set_rg("52456789")
    alunoPortugues5.set_endereco("Rua E")
    alunoPortugues5.set_contato("5595234445")
    alunoPortugues5.set_matricula("05/02/2025")
    alunoPortugues5.set_nota("6.5")
    print(f" Nome: {alunoPortugues5.get_nome()}, \n RG: {alunoPortugues5.get_rg()},\n Endereco: {alunoPortugues5.get_endereco()}, \n Contato: {alunoPortugues5.get_contato()}, \n Matricula: {alunoPortugues5.get_matricula()}, \n Nota: {alunoPortugues5.get_nota()} \n")


    #Criando uma instância da classe AlunoPortugues através do método construtor da classe pai (Aluno)
    print("----------------------------------------------------------------")
    print("Grupo de Alunos de Matemática")
    print("----------------------------------------------------------------")
    alunoMatematica1 = AlunoMatematica()
    alunoMatematica1.set_nome("Glen")
    alunoMatematica1.set_rg("12456789")
    alunoMatematica1.set_endereco("Rua E")
    alunoMatematica1.set_contato("5591234445")
    alunoMatematica1.set_matricula("01/02/2021")
    alunoMatematica1.set_nota("10")
    print(f" Nome: {alunoMatematica1.get_nome()}, \n RG: {alunoMatematica1.get_rg()}, \n Endereco {alunoMatematica1.get_endereco()}, \n Contato: {alunoMatematica1.get_contato()}, \n Matricula: {alunoMatematica1.get_matricula()}, \n Nota: {alunoMatematica1.get_nota()} \n")

    alunoMatematica2 = AlunoMatematica()
    alunoMatematica2.set_nome("Rosa")
    alunoMatematica2.set_rg("226446789")
    alunoMatematica2.set_endereco("Rua J")
    alunoMatematica2.set_contato("5592235545")
    alunoMatematica2.set_matricula("02/02/2021")
    alunoMatematica2.set_nota("10")
    print(f" Nome: {alunoMatematica2.get_nome()}, \n RG: {alunoMatematica2.get_rg()}, \n Endereco {alunoMatematica2.get_endereco()}, \n Contato: {alunoMatematica2.get_contato()}, \n Matricula: {alunoMatematica2.get_matricula()}, \n Nota: {alunoMatematica2.get_nota()} \n")


    alunoMatematica3 = AlunoMatematica()
    alunoMatematica3.set_nome("Meredith")
    alunoMatematica3.set_rg("3246546487")
    alunoMatematica3.set_endereco("Rua I")
    alunoMatematica3.set_contato("5593254654")
    alunoMatematica3.set_matricula("03/02/2021")
    alunoMatematica3.set_nota("10")
    print(f" Nome: {alunoMatematica3.get_nome()}, \n RG: {alunoMatematica3.get_rg()}, \n Endereco: {alunoMatematica3.get_endereco()},\n Contato: {alunoMatematica3.get_contato()},  \n Matricula: {alunoMatematica3.get_matricula()}, \n Nota: {alunoMatematica3.get_nota()} \n")

    alunoMatematica4 = AlunoMatematica()
    alunoMatematica4.set_nome("Lorena")
    alunoMatematica4.set_rg("45671123")
    alunoMatematica4.set_endereco("Rua E")
    alunoMatematica4.set_contato("559565687")
    alunoMatematica4.set_matricula("01/02/2021")
    alunoMatematica4.set_nota("10")
    print(f" Nome: {alunoMatematica4.get_nome()}, \n RG: {alunoMatematica4.get_rg()}, \n Endereco: {alunoMatematica4.get_endereco()}, \n Contato: {alunoMatematica4.get_contato()}, \n Matricula: {alunoMatematica4.get_matricula()},\n Nota: {alunoMatematica4.get_nota()} \n")

    alunoMatmatica5 = AlunoMatematica()
    alunoMatmatica5.set_nome("Fabiano")
    alunoMatmatica5.set_rg("52456789")
    alunoMatmatica5.set_endereco("Rua E")
    alunoMatmatica5.set_contato("5595234445")
    alunoMatmatica5.set_matricula("05/02/2025")
    alunoMatmatica5.set_nota("10")
    print(f" Nome: {alunoMatmatica5.get_nome()}, \n RG: {alunoMatmatica5.get_rg()},\n Endereco: {alunoMatmatica5.get_endereco()}, \n Contato: {alunoMatmatica5.get_contato()}, \n Matricula: {alunoMatmatica5.get_matricula()}, \n Nota: {alunoMatmatica5.get_nota()} \n")


