#TESTING
from config import Test, Dato, Persona

Test()

dato = Dato()
dato.nombre = "Nico"
print(dato.nombre)


persona1 = Persona("NICOLAS")
persona1.saludo()