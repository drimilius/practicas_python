passwords = {"roberto":"abc12345", "juan":"password123", "ivan":"qwertyui", "julis":"1234567","andres":"hola"}
for nombre, password in passwords.items():
    if len(password) < 8:
        print(f"La contraseña {nombre} es muy corta.")
        break
else:
    print("Todos los passwords tiene la longitud requerida")
        
contador=0       
elements= len(passwords)
while contador < elements:
    if len(passwords[contador]) < 8:
        print(f"La contraseña {passwords[contador]} es muy corta.")
        break
    contador +=1
     