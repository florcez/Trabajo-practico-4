#CLASES

class Test:
    def __init__(self):
        print("TEST OK")

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self):
        print("Hola ", self.nombre)