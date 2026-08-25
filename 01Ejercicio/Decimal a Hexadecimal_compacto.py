numero, hexadecimal= "10", ""
if numero == "0":  print("0")
digitos = "0123456789ABCDEF"
while numero > "0": hexadecimal, numero = digitos[int(numero) % 16] + hexadecimal, str(int(numero) // 16)
print(hexadecimal)