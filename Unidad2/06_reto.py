total_cuenta = float(input("Ingrese el total de la cuenta: ")) # Solicita el total de la cuenta
porcentaje_propina = float(input("Ingrese el porcentaje de propina: ")) # Solicita el porcentaje de propina
numero_personas = int(input("Ingrese el número de personas para dividir la cuenta: ")) # Solicita el número de personas

print("Total de la cuenta: $", total_cuenta) # Muestra el total de la cuenta
print("Porcentaje de propina: ", porcentaje_propina, "%") # Muestra el porcentaje de propina
print("Número de personas: ", numero_personas) # Muestra el número de personas

print("------------------------------------------------------------------------") # Línea de separación

total_propina = total_cuenta * (porcentaje_propina / 100) # Calcula el total de la propina
total_por_persona = (total_cuenta + total_propina) / numero_personas # Calcula el total a pagar por persona  
total_cuenta_con_propina = total_cuenta + total_propina # Calcula el total de la cuenta con propina

print("Total de la propina: $", round(total_propina)) # Muestra el total de la propina
print("Total a pagar por persona: $", round(total_por_persona)) # Muestra el total a pagar por persona
print("Total de la cuenta con propina: $", round(total_cuenta_con_propina)) # Muestra el total de la cuenta con propina