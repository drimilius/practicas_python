from cuenta_de_ahorros import CuentaAhorro
def main():
    cuenta1 = CuentaAhorro("roberto Hernandez", 1000)
    print(f"el titular es{cuenta1.titular}")
    print(f"el saldo es:  ${cuenta1.saldo}")
    print(f"La Tasa de interes es: ${cuenta1.tasa_interes * 100}%")
    
    cuenta1.depositar(500)
    cuenta1.retirar(200)
    cuenta1.aplicar_interes()
    
    print(f"el saldo es: ${cuenta1.saldo}")
    
if __name__ == "__main__":
    main()
    
    