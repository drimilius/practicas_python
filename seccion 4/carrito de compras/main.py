from producto import Producto
from carrito import Carrito

try:
    p1 = Producto("laptop", 1000, 5)
    p2 = Producto("Smartphone", 500, 10)
    p3 = Producto("Diadema", 150, 2) 
    carrito = Carrito()
    carrito.agregar_productos(p1, 3)
    carrito.agregar_productos(p2, 4)
    carrito.agregar_productos(p3, 1)
    carrito.mostrar_carrito()
    carrito.eliminar_productos("Smartphone")
    carrito.mostrar_carrito()

except ValueError as  e:
    print(f"Error:{e}")

