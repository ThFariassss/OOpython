class Estudante:
    escola = "Puc"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_Valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Thiago", 1)
aluno_2 = Estudante("Rafaella", 2)
mostrar_Valores(aluno_1, aluno_2)

Estudante.nome = "Python"
aluno_3 = Estudante("Guilherme", 3)
mostrar_Valores(aluno_1, aluno_2, aluno_3)


