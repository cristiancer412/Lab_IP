operador = input("Ingrese el operador (+, -, *, /): ")
num1=input("Ingrese el primer número: ")
num2=input("Ingrese el segundo número: ")
resultado = num1+operador+num2
resultado = eval(resultado)
print("El resultado de la operación es: ", resultado)