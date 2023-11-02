#
# autor: Pedro Rogério
# data: 01/11/2023

from disciplina import Disciplina

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def listar_disciplinas(self):
        print(f"Disciplinas do professor {self.nome}:")
        for disciplina in self.disciplinas:
            print(disciplina.nome)
