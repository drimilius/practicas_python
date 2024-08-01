import random
#generar un numero secreto entre 1 y 10
numero_secreto = random.randint(1, 10)
#pedir al usuario que adivine el numero secreto
adivinanza = int(input("Adivine el numero secreto (entre 1 y 10): "))

#comparar el numero ingresado con el numero secreto
if adivinanza == numero_secreto:
    print("Felicidades! Adivinaste el numero secreto.")
elif adivinanza < numero_secreto:
    #print("tu numero no es correcto")
    print("Tu numero no es correcto. El numero secreto era menor que", numero_secreto)
else:
    #print("tu numero no es correcto")
   print("Tu numero no es correcto. El numero secreto era", numero_secreto)
    
    