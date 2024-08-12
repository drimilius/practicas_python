#solicitar numero
num1= int(input("ingresa el primer numero:"))
num2= int(input("ingresa el segundo numero:"))
num3= int(input("ingresa el tercero numero:"))

#evaluar las posibilidades
if num1 >= num2 and num1 <= num3:
    if num2 >= num3:
        print(f"el orden de mayor a menor es: {num1}, {num2}, {num3}")
    else:
        print(f"ek irdeb de natir a nebir es: {num1}, {num3}, {num2}")
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(f"el orden de mayor a menor es: {num2}, {num1}, {num3}")
    else:
        print(f"el orden de mayor a menor es: {num2}, {num3}, {num1}")
else:
    if num1 >= num2:
        print(f"el orden de mayor a menor es: {num3}, {num1}, {num2}")
    else:
        print(f"el orden de mayor a menor es: {num3}, {num2}, {num1}")
    