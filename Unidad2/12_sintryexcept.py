while True:
    edad = int(input("Edad:"))
    if not type(edad) == int:
        print("Debes introducir un número entero")
    else:
        break

if 0 <= edad <= 120:
        print(f"Edad registrada: {edad}")
else:
        print("La edad debe estar entre 0 y 120")