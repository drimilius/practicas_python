import json
with open("files/json/employees.json", "r") as file:
    data = json.load(file)
    
#operaciones basicas

for employee in data["employees"]:
    print(f"Nombre: {employee["name"]},Edad:{employee["age"]}, Ciudad: {employee["city"]}")

total_age = sum(employee["age"] for employee in data["employees"])
average_age = total_age /len(data["employees"])

print(f"La edad promedio de los empleados es: {average_age}")

city = "London"
employees_in_city = [emp["name"] for emp in data["employees"] if emp ["city"] == city]
print(f"\n Empleado en la ciudad {city}: {",".join(employees_in_city)}")

New_employee = {"name": "Roberto", "age": 38, "city": "Tlaxcala"}
data["employees"].append(New_employee)
#guardar los cambios

with open("files/json/employees.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nEmpleado agregado correctamente")


