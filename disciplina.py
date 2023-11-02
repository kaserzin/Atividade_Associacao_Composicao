#
# autor: Pedro Rogério
# data: 01/11/2023

from atividade import Atividade

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.atividades = []

    def adicionar_atividade(self, atividade):
        datas_existentes = [a.data for a in self.atividades]
        if atividade.data not in datas_existentes:
            self.atividades.append(atividade)
        else:
            print("Já existe uma atividade nesta data.")

    def listar_atividades_em_aberto(self):
        print(f"Atividades em aberto da disciplina {self.nome}:")
        for atividade in self.atividades:
            if not atividade.concluida:
                print(atividade)

    def listar_atividades_concluidas(self):
        print(f"Atividades concluídas da disciplina {self.nome}:")
        for atividade in self.atividades:
            if atividade.concluida:
                print(atividade)