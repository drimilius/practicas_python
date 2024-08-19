from abc import ABC,abstractmethod
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass
 
#clase hija que procesa pago para tarjeta de credito
class PagoTarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago con tarjeta de credito, monto: {monto}")  
    def ValidarNumeroTarjeta(self,numeroTarjeta):
        print(f"Validar numero tarjeta {numeroTarjeta}")

#segunda clase hija que procesa

class PagoPaypal(ABC):
    def procesar_pago(self, monto):
        print(f"Procesando pago con PayPal, monto: {monto}")

#clase hija pago criptomoneda

class PagoCriptomoneda(MetodoPago, PagoPaypal):
    def procesar_pago(self, monto):
        print(f"Procesando pago con criptomoneda, monto: {monto}")

#instanciar objetos

def realizar_pago(metodo_pago, monto):
    metodo_pago.procesar_pago(monto)
        
#main
pago1 = PagoTarjetaCredito()
pago2 = PagoPaypal()
pago3 = PagoCriptomoneda()
pago1.ValidarNumeroTarjeta("1234567890")

realizar_pago(pago1, 100)
realizar_pago(pago2, 300)
realizar_pago(pago3, 500)

