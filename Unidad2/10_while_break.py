while True:
    opcion = input("elige A,B o C: "). strip().upper()
    if opcion in ("A","B","C"):
        break
    print ("opcion incorrecta, vuelve a intentarlo")

print (f"opcion correcta: {opcion}") # Opción seleccionada