x=10
if x > 5:
    print("x es mayor que 5")
    
    #if: primera condiciion 
    #elif: segunda condicion
    #else: ultima condicion, se ejecuta un bloque de codigo cuando la condicion ya no devuelve true
    #if condicon (bloque de codigo)> condicion =true
    #elif condicion2 (bloque de codigo)> condicion =false condicion2 = true
    #else bloque de codigo > condicion=false , condicion2 =false
    
      
    
x = 7
if x > 10:
    print("x es mayor que 10") 
elif x > 5:
    print("x es mayor que 5 pero menor o igual que 10")
else: #se ejecuta un bloque de codigo cuando la condicion ya no devuelve true
    print("x es menor o igual que 5")

y= int(input("Ingrese un numero: "))
if y <10:
    print("El numero es menor que 10")
elif y == 10:
    print("El numero es igual a 10")
elif y < 20: 
    print("El numero es mayor que 10 pero menor que 20")
else:
    print("El numero es mayor que 20")
                                 

edad=int(input("Ingrese su edad: "))
if edad < 18:
    print("debe tener al menos 18 años para registrarse")
elif edad <= edad <=120:
    print("registro exitoso. bienvenido")
else:
    print("Edad no valida. Por favor ingrese una edad valida")         