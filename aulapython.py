class MinhaClasse:
    """
    Documentacao da Classe
    """
    atributo_publico = None
    __atributo_privado = 5

    def __init__(self):
        self.atributo_publico = 10
        def metodo(self):
            return self.atributo_publico * 2

        def get_atributo_privado(self):
            return self.__atributo_privado


a = MinhaClasse()

print(a.atributo_publico)

print(a.get_atributo_privado())
