from cuenta_de_ahorros import CuentaAhorro
def main():
    cuenta1 = CuentaAhorro("roberto Hernandez", 1000)
    cuenta2 = CuentaAhorro("Ivan", 3000)
    print(f"el titular es{cuenta1.titular}")
    print(f"el saldo es:  ${cuenta1.saldo}")
    print(f"La Tasa de interes es: ${cuenta1.tasa_interes * 100}%")
    
    cuenta1.depositar(500)
    cuenta1.retirar(200)
    cuenta1.aplicar_interes()
    
    print(f"el saldo es: ${cuenta1.saldo}")
    
    cuenta2.depositar(3000)
    cuenta2.retirar(200)
    cuenta2.aplicar_interes()
    print(f"el titular es{cuenta2.titular}")
    print(f"el saldo es:  ${cuenta2.saldo}")
    print(f"La Tasa de interes es: ${cuenta2.tasa_interes * 100}%")
    
    
if __name__ == "__main__":
    main()
    
    