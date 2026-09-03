for numero in range (1, 7): #trabajando rango con for
    cuadrado = numero ** 2
    print (numero, cuadrado)

materias= ["Python", "Linux", "Interfaces" ]
for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion}, {materia}")

    cadena= "0123456789ABCDE"
    for letra in cadena:
        print(letra)

for i in range(len(cadena)):
    print(cadena[i])