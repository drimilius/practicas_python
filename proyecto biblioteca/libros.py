from material_biblioteca import MaterialBiblioteca

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, numero_de_paginas):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_de_paginas = numero_de_paginas
    
    def informacion(self):
        print(f"{super().informacion()}, Número de Páginas: {self.numero_de_paginas}")
    
