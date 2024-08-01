#lista(list)
frutas= ["tunas", "peras", "uva", "melon"]
numeroPrimos=[2, 3, 5, 7, 11]

print(type(frutas))
print(type(numeroPrimos))
print(frutas[0])
print(numeroPrimos[3])


frutas[0]="mango"
print(frutas)

frutas.append("manzana") #agrega un elemento al final de la lista frutas
print(frutas)

numeroPrimos.append("13") #Intento de agregar un elemento que no es un numero primo
print(numeroPrimos)

#tupla
dimensiones=(1920.1080)
coordenadas=(10,20)
print(type(dimensiones))
print(type(coordenadas))

#puntos=(10,20) no se puede asignar a tupla un nuevo valor 
#puntos[1]=30


#conjunto
colores={"rojo", "azul", "verde"}
numero_unicos={1,2,3,4,5}
print(type(colores))
print(type(numero_unicos))
print(colores)
print(numero_unicos)
numero_unicos.add(6) #agrega un elemento al conjunto numero_unicos
colores.remove("rojo") #remueve un elemento del conjunto colores

len(numero_unicos) #cuenta el numero de elementos en el conjunto
print (len(colores)) #cuenta el numero de elementos en el conjunto
print (len(colores)) #cuenta el numero de elementos en el conjunto)

#diccionario

personas={"nombre":"Juan", "apellido":"Perez", "edad":30, "Ciudad":"Lima"} #tiene una clave-valor
precios={"manzana":12, "pera":5, "uva":2.5}
print(type(personas))
print(type(precios))
print (personas["nombre"]) #imprime el valor de la clave "nombre"
print(precios["uva"])             #imprime el valor de la clave "uva"
personas["apellido"]="Gomez" #modifica el valor de la clave "apellido"
print(personas)
personas["ocupacion"]="ingeniero" #agrega una nueva clave-valor
print(personas)


