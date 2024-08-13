#diccionario estudiantes
estudiantes = [
    {"nombre":"Juan", "edad":17, "calificaciones": [85, 90, 88]},
    {"nombre":"Maria", "edad":19, "calificaciones": [92, 89, 90]},
    {"nombre":"Pedro", "edad":21, "calificaciones": [85, 95, 80]},
    {"nombre":"Ana", "edad":18, "calificaciones": [90, 92, 87]},
    {"nombre":"Luis", "edad":20, "calificaciones": [88, 85, 92]},
]

for estudiante in estudiantes:
    edad = estudiante["edad"]
    calificaciones = estudiante["calificaciones"]
    promedio_calificaiones = sum(calificaciones) / len(calificaciones)
    
    if edad > 18 and promedio_calificaiones > 85:
        print(f"nombre: {estudiante["nombre"]}, Edad: {edad}, promedio: {promedio_calificaiones:.2f}")

#Calculo de numeros primos
primos=[] 
for estudiante in estudiantes:
    edad = estudiante["edad"]
    
    #verificar si la edad es numero primo (calcular numeros primos )
    if edad > 18:
        es_primo = True
        if edad <= 1:
            es_primo = False
        else:
            for i in range(2, int(edad ** 0.5)+ 1):
                if edad % i == 0:
                    es_primo = False
                    break
        if es_primo:
            primos.extend(estudiante["calificaciones"])
        
#calcular
if primos:
    promedio_primo = sum(primos) / len(primos)
    print(f"\nPromedio de calificiones de estudiantes mayores de 18 años con edad primo: {promedio_primo:.2f}"  )
else:
    print("\nNo hay estudiantes mayores de 18 años con edad de numeros primos.")    