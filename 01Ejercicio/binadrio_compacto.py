numero, binario = 10, "" # número a convertir a binario y variable para almacenar el resultado
if numero == 0: print("0") # si el número es 0, imprimir 0
while numero > 0: binario = str(numero % 2) + binario; numero //= 2 # mientras el número sea mayor que 0, calcular el residuo de la división entre 2 y agregarlo al inicio de la cadena binaria, luego dividir el número entre 2
print(binario) # imprimir el resultado final