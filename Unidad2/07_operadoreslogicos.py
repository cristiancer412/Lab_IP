edad= 18
tiene_credencial = True
tiene_adeudo = False

es_mayor = edad >= 18
documento_valido = tiene_credencial
sin_adeudo = not tiene_adeudo

if es_mayor:
    if documento_valido:
        if sin_adeudo:
            autorizado = True
        else:
            autorizado = False
    else:
        autorizado = False
else:
    autorizado = False

print(autorizado)