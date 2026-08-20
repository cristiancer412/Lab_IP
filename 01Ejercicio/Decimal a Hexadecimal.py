numero, hex_digits = "10", "0123456789ABCDEF"
if numero == "0": print("0")
else:
        hexadecimal = ""
        while numero > "0":
                residuo = int(numero) % 16
                hexadecimal = hex_digits[residuo] + hexadecimal
                numero = str(int(numero) // 16) 
print(hexadecimal)