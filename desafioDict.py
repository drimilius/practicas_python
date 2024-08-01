#obtencion de datos del usuario

nombre = input("introduce tu nombre:  ") #obtener datos del usuario input=comando para obtener datos
email = input("introduce el email de contacto: ") #obtener datos del usuario
telefono = input("introduce el telefono de contacto: ") #obtener datos del usuario

#almacenar datos en un diccionario
contacto = {
    "nombre": nombre, #datos almacenados del diccionario
    "email": email, 
    "telefono": telefono  
}

#realiza 
num_caracteres_nombre = len(contacto["nombre"]) #conteo de caracteres en el nombre

#impresion de los resultados
print("\nInformacion del contacto:") #\n para saltar una linea
print(f"Nombre:", contacto["nombre"]) #f-string para interpolar variables
print(f"Email:", contacto["email"]) 
print(f"Telefono:", contacto["telefono"])
print(f"Numero de caracteres en el nombre: {num_caracteres_nombre}")
