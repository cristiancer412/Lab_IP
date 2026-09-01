numero, hexadecimal= 9, "" # número a convertir a hexadecimal y variable para almacenar el resultado
if numero == 0:  print("0") # si el número es 0, imprimir 0
digitos = "0123456789ABCDEF" # lista de dígitos hexadecimales
while numero > 0: # mientras el número sea mayor que 0, continuar dividiendo entre 16
    hexadecimal = digitos[numero % 16] + hexadecimal # obtener el dígito hexadecimal correspondiente al residuo de la división entre 16 y agregarlo al resultado
    numero //= 16 # dividir el número entre 16 y actualizar su valor
print(hexadecimal) # imprimir el resultado final