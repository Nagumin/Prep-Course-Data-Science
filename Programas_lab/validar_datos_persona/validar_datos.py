def es_mayor_de_edad(edad):
    return edad >= 18

def crear_contrasena():
    while True:
        contrasena = input("Crea una contraseña: ")
        confirmar_contrasena = input("Confirma tu contraseña: ")

        if contrasena == confirmar_contrasena:
            print("Contraseña creada exitosamente.")
            return contrasena
        else:
            print("Las contraseñas no coinciden. Inténtalo de nuevo.")

def validar_datos_persona():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))

    if es_mayor_de_edad(edad):
        print(f"Hola, {nombre}. Eres mayor de edad.")
        contrasena = crear_contrasena()
    else:
        print(f"Lo siento, {nombre}. Debes ser mayor de edad para continuar.")

validar_datos_persona()
