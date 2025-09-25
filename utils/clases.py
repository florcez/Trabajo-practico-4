#CLASES

class libro:

    #---------------INFO---------------------
    def __init__(self, name):
        self.name = name

    def getAutor(self,autor):
        self.autor = autor
    
    def getGenero(self,genero):
        self.genero = genero
    
    def getYear(self, year):
        self.year_publicacion = year
    
    def getDisponible(self, disponible):
        self.disponible = disponible
    #---------------------------------------------

    def prestar(self):
        if self.disponible == True:
            self.disponible = False
    
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
    
    def esAntiguo(self):
        if 2025 -self.year_publicacion > 20:
            return True
    
    def mostrarInfo(self):
        info = [self.name, self.autor, self.genero, self.year_publicacion, self.disponible]
        return info
    

class Biblioteca:
    def __init__(self):
        self.listaLibros = {}
    
    def agregarLibro(self, libro):
        self.listaLibros.append(libro)
    
    def listarLibros(self):
        return self.listaLibros
    
    def prestarPorTitulo(self, titulo):
        for i in range(self.listaLibros):
            if self.listaLibros[i-1][0].lower() == titulo.lower():
                return True
    
    def devolverPorTitulo(self, titulo):
        for i in range(self.listaLibros):
            if self.listaLibros[i-1][0].lower() == titulo.lower():
                return True