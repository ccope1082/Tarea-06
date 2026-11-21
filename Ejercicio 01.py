# Función para ingresar los paquetes
def ingresar_paquetes():
    paquetes = []

    for i in range(5):
        while True:
            cantidad = int(input(f"Ingrese la cantidad de paquetes del día {i + 1}: "))

            if cantidad >= 0:
                paquetes.append(cantidad)
                break
            else:
                print("Error: la cantidad no puede ser negativa.")

    return paquetes


# Función para mostrar el vector
def mostrar_vector(paquetes):
    print("\nCantidades registradas:")
    for cantidad in paquetes:
        print(cantidad, end=" ")
    print()


# Función para calcular el total
def calcular_total(paquetes):
    return sum(paquetes)


# Función para obtener la cantidad mayor
def obtener_mayor(paquetes):
    return max(paquetes)


# Función para contar los días con más de 20 paquetes
def contar_dias_mas_20(paquetes):
    contador = 0

    for cantidad in paquetes:
        if cantidad > 20:
            contador += 1

    return contador


# Programa principal
paquetes = ingresar_paquetes()

mostrar_vector(paquetes)

print("\nTotal de paquetes procesados:", calcular_total(paquetes))
print("Cantidad mayor registrada:", obtener_mayor(paquetes))
print("Días con más de 20 paquetes:", contar_dias_mas_20(paquetes))
