numero, octal = 10, "" # número a convertir a octal y variable para almacenar el resultado
if numero == 0: print("0") # si el número es 0, imprimir 0
while numero > 0: octal = str(numero % 8) + octal; numero //= 8 # mientras el número sea mayor que 0, calcular el residuo de la división entre 8 y agregarlo al inicio de la cadena octal, luego dividir el número entre 8
print(octal)