numero = 9
hex_digits = "0123456789ABCDEF"
if numero == 0:
        print("0")

else:
        hexadecimal = ""
        while numero > 0:
                residuo = numero % 16
                hexadecimal = hex_digits[residuo] + hexadecimal
                numero = numero // 16
        print(hexadecimal)