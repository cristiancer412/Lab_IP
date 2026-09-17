edad = 17
tiene_credencial = True
tiene_adeudo =  True

if edad >=18:
    es_mayor = True
else:
    es_mayor = False

tiene_credencial = True
sin_adeudo = not tiene_adeudo

if es_mayor and tiene_credencial and sin_adeudo:
    autorizado = True
else:
    autorizado = False
print(autorizado)