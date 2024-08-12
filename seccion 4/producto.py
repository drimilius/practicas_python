class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_datos(self):
        return f"El producto: {self.nombre} \n Precio: {self.precio} \n stock: {self.stock}"
    def agregar_stock(self, stock):
        self.stock += stock
        print(f"se an agregado {stock} al stock del producto {self.nombre}, la cantidad actual es {self.stock}")

    def vender(self, stock):
        if stock > self.stock:
            print(f"no hay suficiente stock del producto {self.nombre}, la cantidad actual es {self.stock}")
        else:
            self.stock -= stock
            print(f"se vendio {stock} del producto {self.nombre}, la cantidad actual es {self.stock}")
            
#main
nombre_pr1=input("ingresa el producto 1")
precio_pr1=int(input("ingresa el precio del producto 1"))
cantidad_pr1=int(input("ingresa la cantidad del producto 1"))
producto1= Producto(nombre_pr1, precio_pr1, cantidad_pr1)
producto2 = Producto("mesa", 200, 30)

print(producto1.mostrar_datos())
print(producto2.mostrar_datos())
producto1.agregar_stock(10)
print(producto1.mostrar_datos())
producto2.vender(15)
print(producto2.mostrar_datos())
producto1.vender(40)
print(producto1.mostrar_datos())



    
        