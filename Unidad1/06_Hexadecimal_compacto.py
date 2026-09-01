numero, hexadecimal= "10", "" # número a convertir a hexadecimal y variable para almacenar el resultado
if numero == "0":  print("0") # si el número es 0, imprimir 0
digitos = "0123456789ABCDEF" # lista de dígitos hexadecimales
while numero > "0": hexadecimal, numero = digitos[int(numero) % 16] + hexadecimal, str(int(numero) // 16) # mientras el número sea mayor que 0, calcular el residuo de la división entre 16 y agregarlo al inicio de la cadena hexadecimal, luego dividir el número entre 16
print(hexadecimal) # imprimir el resultado final