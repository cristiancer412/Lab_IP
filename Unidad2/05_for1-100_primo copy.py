for numero in range(2, 100):
    es_primo = [i for i in range(2, numero) if numero % i == 0]
    if len(es_primo) == 0: print(numero)