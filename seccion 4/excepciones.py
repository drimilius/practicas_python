class EdadinvalidError(Exception):
    pass
def verificarEdad(edad):
    if edad < 18:
        raise ValueError("debe ser mayor de 18 años para registrarse")
    return "registro completo"
try:
    mensaje = verificarEdad(20)
    print(mensaje)
except ValueError as e:
    print(f"error {e}")