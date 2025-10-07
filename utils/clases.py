#CLASES

class Libro:   #define la clase libro

    #---------------INFO---------------------
    def __init__(self, name, autor, genero, year):    #pide datos
        self.name = name   #define nombre
        self.autor = autor   #define autor
        self.genero = genero   #define genero
        self.year_publicacion = int(year)   #define año de publicación
    
        self.disponible = True    #define que está disponible

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
        if self.disponible == True:   #Si el libro está disponible
            self.disponible = False   #el libro ya no está disponible
    
    def devolver(self):
        if self.disponible == False:   #si no esta disponible
            self.disponible = True   #ahora está disponible
    
    def esAntiguo(self):
        if 2025 - self.year_publicacion > 20:   #si es mayor a 20 años es antiguo
            return True
    
    def mostrarInfo(self):
        info = [self.name, self.autor, self.genero, self.year_publicacion, self.disponible]
        #guarda toda la informacion de la clase en una lista
        return info
    
    

class Biblioteca:
    def __init__(self):
        self.listaLibros = []   #define la lista de libros
    
    def agregarLibro(self, libro):
        self.listaLibros.append(libro)   #agrega un libro a la lista
    
    def listarLibros(self): 
        return self.listaLibros   
    
    def titulodispo(self):   #une en una lista el titulo y la disponibilidad del libro
        tituloDispo = []
        for i in range(len(self.listaLibros)):
            td = []
            td.append(self.listaLibros[i].mostrarInfo()[0])
            if self.listaLibros[i].mostrarInfo()[4] == True:
                td.append("Disponible")
            else:
                td.append("No disponible")

            tituloDispo.append(td)
        return tituloDispo

    def buscarLibro(self,titulo):
        for i in range(len(self.listaLibros)):   #repite por la cantidad de libros que hay en la lista
            if self.listaLibros[i].mostrarInfo()[0].lower() == titulo.lower():
                name = self.listaLibros[i].mostrarInfo()[0]
                autor = self.listaLibros[i].mostrarInfo()[1]
                genero = self.listaLibros[i].mostrarInfo()[2]
                año = self.listaLibros[i].mostrarInfo()[3]
            return name, autor, genero, año    #devuelve las variables

    def prestarPorTitulo(self, titulo):
        for i in range(len(self.listaLibros)):   #repite por la cantidad de libros que hay en la lista
            if self.listaLibros[i].mostrarInfo()[0].lower() == titulo.lower():
            #si el nombre del elemento es = al titulo ingresado
                self.listaLibros[i].prestar()   #presta ese elemento
    
    def devolverPorTitulo(self, titulo):
        for i in range(len(self.listaLibros)):   #repite por la cantidad de libros que hay en la lista
            if self.listaLibros[i].mostrarInfo()[0].lower() == titulo.lower():
             #si el nombre del elemento es = al titulo ingresado
                self.listaLibros[i].devolver()   #devuelve  ese elemento


    
    def filtrarAntiguo(self):
        antiguo = []
        for i in range(len(self.listaLibros)):   
            if self.listaLibros[i].esAntiguo() == True:   #verifica si es antiguo
                antiguo.append(self.listaLibros[i])   #lo agrega a la lista de antiguos
        return antiguo
