#metodo
def sin_retorno():
    print("Esta funcion no tiene retorno") #metodo sin retorno

def retorno_unico(a,b):
    return a + b
    print("Este metodo tiene un retorno") #metodo con retorno
    
#main

sin_retorno()
x=5
y=20
retorno2=retorno_unico(x,y)
print(f"el retorno unico es: {retorno2} ")


