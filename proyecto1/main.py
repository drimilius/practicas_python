from coche import Coche

def main():
    coche1 = Coche("Ford", "Mustang", 4)
    coche2 = Coche("Chevrolet", "Corvette", 4)
    coche1.arrancar()
    coche1.abrir_puertas()
    coche1.detener()
    coche2.arrancar()
    coche2.abrir_puertas()
    coche2.detener()
    
if __name__ == "__main__":
    main()
    
    
