# Definición de la función calcular_descuento
def calcular_descuento(total_compra, porcentaje_descuento=10):
    descuento_calculado = (total_compra * porcentaje_descuento) / 100
    return descuento_calculado

# Ingreso del monto total de la primera compra (descuento fijo del 10%)
compra_1 = float(input("Ingresa el monto total de la compra: "))
descuento_1 = calcular_descuento(compra_1)
total_final_1 = compra_1 - descuento_1

# Ingreso del monto total de la segunda compra (descuento fijo del 10%)
compra_2 = float(input("Ingresa el monto total de la segunda compra: "))
descuento_2 = calcular_descuento(compra_2)
total_final_2 = compra_2 - descuento_2

# Mostrar resultados
print(f"Monto total: ${compra_1:.2f}, Descuento aplicado: ${descuento_1:.2f}, Monto final: ${total_final_1:.2f}")
print(f"Monto total: ${compra_2:.2f}, Descuento aplicado: ${descuento_2:.2f}, Monto final: ${total_final_2:.2f}")
