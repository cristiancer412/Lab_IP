def login():
    USUARIO = "alumno"
    CLAVE = "python123"

    usuario = input("Usuario: ").strip().lower()  # lower() hace minúsculas el texto 
    clave = input("Contraseña: ")

    if usuario == USUARIO and clave == CLAVE:
        print("Bienvenido")
        main()  # Si acierta, entra al menú principal del cajero
    else:
        print("Credenciales incorrectas")
        login()  # Si falla, vuelve a pedir las credenciales

def consultar_saldo():  # def sirve para crear funciones
    print("Saldo: $0.00")

def depositar():
    print("Depósito realizado")

def retirar():
    print("Retiro realizado")

def salir():
    print("Saliendo del cajero automático...")

def mostrar_menu():
    print("-----------------------------------")
    print("Bienvenido al cajero automático")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    print("------------------------------------")
    return input("Opción: ").strip()

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            salir()
            break  # Rompe el while y termina el programa
        else:
            print("Opción inválida")

# Iniciamos el programa llamando a login
login()