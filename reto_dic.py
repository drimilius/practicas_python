nombres= {
"cientificos": ["Marie Curie", "Nikola Tesla", "Galileo Galilei", "Ada Lovelace"],
"deportistas": ["Cristiano Ronaldo", "Roger Federer", "Serena Williams", "Rafael Nadal", "Michael Jordan"],
"otros": []
}
#funcion para honrar
def honrar(nombres):
    for nombre in nombres:
        if nombres [nombre] == "cientifico":
            nombres [nombre] = "El honorable" + nombre
    return nombres
        
#funcion para mostrar nombres
def mostrar(nombres, categoria):
    for nombre, tipo in nombres.items():
        if tipo == categoria or (categoria ==  "otros" and tipo not in ["cientifico", "deportista"] ):
            print (nombre)    
    
#lista completa
print("lista completa de nombres")
for nombre in nombres:
    print (nombre)

#honrar a los cientificos
nombre = honrar(nombres)

#mostrar nombre de honorables, deportitas y otros
print("\nCientificos honorables:")
mostrar(nombres, "El honorable")

print("\nDeportistas:")
mostrar(nombres, "Deportista")

print("\nOtros:")
mostrar(nombres, "otros")
    