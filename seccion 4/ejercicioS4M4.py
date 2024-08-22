class Libro:
    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo
    
    def imprimir_info(self):
        print(f"Autor: {self.autor}, Título: {self.titulo}")
        
class LibroPublicacion(Libro):
    def __init__(self, autor, titulo, año_publicacion):
        super().__init__(autor, titulo)
        self.año_publicacion = año_publicacion
    
    def imprimir_info(self):
        print(f"Autor: {self.autor}, Titulo: {self.titulo}, año_publicacion: {self.año_publicacion}")
        
libro_1 = Libro("Dan Brown", "inferno")

libro_2 = LibroPublicacion("Dan Brown", "El Codigo Da Vinci", 2003)

print(libro_1.__dict__)
print(libro_2.__dict__)


