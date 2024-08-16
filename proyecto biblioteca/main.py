from libros import Libro
from revistas import Revista
from periodicos import Periodico

def main():
    libro1 = Libro("El Hobbit", "J.R.R. Tolkien", 1937, 310)
    revista1 = Revista("National Geographic", "Varios", 2023, 800)
    periodico1 = Periodico("El País", "Varios", 2024, "15-08-2024")
    
    print(libro1.informacion())
    print(revista1.informacion())
    print(periodico1.informacion())

if __name__ == "__main__":
    main()     