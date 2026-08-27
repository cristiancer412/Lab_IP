n = int(input("Ingrese un número: "))
es_primo = True
if n<=1:
    es_primo = False
else:
    i=2
    while i<n:
        if n%i==0:
            es_primo = False
            break
        i+=1
if es_primo:
    print("es primo")

    a,b=0,1
    while a<n:
        siguiente = a + b
        a=b
        b=siguiente
    if a==n:    
        print("es fibonacci")
    else:
        print("no es fibonacci")
else:
    print("no es primo") 