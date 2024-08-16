class Cuenta:
    def __init__(self, titular, saldo=0):
        self._titular = titular #atributo protegido
        self._saldo = saldo
        
    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print (" el saldo no puede ser negativo")
        else:
            self._saldo = nuevo_saldo
    def depositar(self, nuevo_saldo):
        if nuevo_saldo > 0:
            self._saldo += nuevo_saldo
            print(f"Se ha depositado {nuevo_saldo} en su cuenta. Nuevo saldo: {self._saldo}")
        else:
            print("No se puede depositar cero o un valor negativo")            

    def retirar(self, nuevo_saldo):
        if 0 < nuevo_saldo <= self._saldo:
            self._saldo -= nuevo_saldo
            print(f"Se ha retirado {nuevo_saldo} de su cuenta. Nuevo saldo: {self.saldo}")
        else:
            print("No se puede retirar cero o un valor negativo o mayor al saldo")
            
            