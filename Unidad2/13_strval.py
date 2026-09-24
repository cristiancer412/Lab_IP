
while True: 
    nombre = input("Nombre: ")
    
    # Limpia espacios extra de los extremos y del medio
    nombre_limpio = " ".join(nombre.split())

    if nombre_limpio and nombre_limpio.replace(" ", "").isalpha():
        break

    print("Usa letras y no dejas el nombre vacío.")

nombre_normalizado = nombre_limpio.title()
print(f"Hola, {nombre_normalizado}")