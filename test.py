#TESTING
from config import *
from utils.clases import *
biblio = Biblioteca()

def menu():
    print("1-AGREGAR LIBRO",
              "2-LISTAR LIBROS",
              "3-PRESTAR LIBRO",
              "4-DEVOLVER LIBRO",
              "5-FILTRAR ANTIGUOS")
    x = int(input())
    return x


while True:
   

    x = menu()
    if x == 1:
        print("Nombre del libro")
        nom = input()

        print("Nombre del autor")
        autor = input()
        
        print("Genero del libro")
        genero = input()

        print("Año de publicación")
        año = input()
        
        libro = Libro(nom, autor, genero, año)
        biblio.agregarLibro(libro)
   

    
    if x == 2:
        lista = biblio.listarLibros()
        for elemento in lista:
            print(elemento.mostrarInfo())

    if x == 3:
        print("Ingresar el titulo que queres prestar")
        titulo = input()
        biblio.prestarPorTitulo(titulo)
    if x == 4:
        print("Ingresar el titulo que queres devolver")
        titulo = input()
        biblio.devolverPorTitulo(titulo)
    if x == 5:
        print("Filtrar antiguos")
        antiguo = biblio.filtrarAntiguo()

        for elem in antiguo:
            print(elem.mostrarInfo())