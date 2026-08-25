n = int(input("Ingrese un número: "))
i=2
if n<2:
    print("es primo")
else:
    while i*i<=n:
        if n%i==0:
            print("no es primo")
            break
        i=i+1
    else:
        print("es primo")    