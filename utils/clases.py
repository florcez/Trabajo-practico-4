#CLASES

class Libro:

    #---------------INFO---------------------
    def __init__(self, name, autor, genero, year):
        self.name = name
        self.autor = autor
        self.genero = genero
        self.year_publicacion = int(year)
    
        self.disponible = True

    def getAutor(self):
        return self.autor
    
    def getGenero(self):
        return self.genero
    
    def getYear(self):
        return self.year_publicacion
    
    def getDisponible(self):
        return self.disponible 
    #---------------------------------------------

    def prestar(self):
        if self.disponible == True:
            self.disponible = False
    
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
    
    def esAntiguo(self):
        if 2025 - self.year_publicacion > 20:
            return True
    
    def mostrarInfo(self):
        info = [self.name, self.autor, self.genero, self.year_publicacion, self.disponible]
        return info
    

class Biblioteca:
    def __init__(self):
        self.listaLibros = []
    
    def agregarLibro(self, libro):
        self.listaLibros.append(libro)
    
    def listarLibros(self):
        return self.listaLibros
    
    def prestarPorTitulo(self, titulo):
        for i in range(len(self.listaLibros)):
            if self.listaLibros[i].mostrarInfo()[0].lower() == titulo.lower():
                self.listaLibros[i].prestar()
    
    def devolverPorTitulo(self, titulo):
        for i in range(len(self.listaLibros)):
            if self.listaLibros[i].mostrarInfo()[0].lower() == titulo.lower():
                self.listaLibros[i].devolver()
