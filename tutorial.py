class Pai:

    # Atributos da classe, fixo para todas as classes
    sexo = "Masculino"

    # Atributos das instâncias
    def __init__(self, nome):
        self.nome = nome

    # Métodos das instâncias
    def print_nome(self):
        print(self.nome)

# Herança
class Filho(Pai):
    pass     