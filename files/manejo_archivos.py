with open("files/ejemplo.txt","w") as file:
    file.write("Esto es un ejemplo de escritura en un archivo.")    
    file.write("\nEsta es la segunda línea.")
    file.write("\nEsta es la tercera línea.")

with open("files/ejemplo.txt","r") as file:
    
    print(file.read())
    
with open("files/ejemplo.txt","a") as file:
    file.write("\nEsta es la cuarta línea agregada.")
    file.write("\nEsta es la quinta línea agregada.")
    
with open("files/ejemplo.txt","r") as file:
    
    print(file.read())
