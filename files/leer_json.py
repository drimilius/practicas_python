import json

with open("files/json/data.json", "r") as file:
    datos = json.load(file)
    

nombre = datos["nombre"] 
edad=datos["edad"]
correo = datos["correo"]
hobbies = datos["hobbies"]
trabajo = datos["trabajo"]
empresa = datos["trabajo"]["empresa"]
puesto = datos["trabajo"]["puesto"]
años = datos["trabajo"]["años"]

print(f"Nombre:{nombre}")
print(f"Edad:{edad}") 
print(f"Correo:{correo}")
print(f"Hobbies:{hobbies}")
print(f"Trabajo:{trabajo}")
print(f"empresa:{empresa}")
print(f" puesto:{puesto}")
print(f" años:{años}")


# Mostrar todos los empleados
print("Lista de empleados")

for employee in datos["employees"]:
    print(f"Nombre:{employee["nombre"]}, Puesto:{employee["puesto"]}")    