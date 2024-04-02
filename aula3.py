class Aluno:
    def __init__(self): #construtor
        self.nome = "" #atributos
        self.matricula = ""
    def ano_ingresso(self): #método
        return int(self.matricula[0:4])


a = Aluno()
a.nome = "Rafaela"
a.matricula = "20231011110005"
b = Aluno() #cria-se primeiro a variável chamando a classe para depois configurar os outros elementos presentes nessa classe
b.nome = "Miguel"
b.matricula = "20231011110022"

print(a.nome, a.matricula, a.ano_ingresso)
print(b.nome, b.matricula, b.ano_ingresso)