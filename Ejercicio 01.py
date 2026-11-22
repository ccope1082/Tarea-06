# Función para ingresar los paquetes
def Ingresar_Paquetes():
    Paquetes = []

    for i in range(5):
        while True:
            Cantidad = int(input(f"Ingrese la cantidad de paquetes del día {i + 1}: "))

            if Cantidad >= 0:
                Paquetes.append(Cantidad)
                break
            else:
                print("Error: la cantidad no puede ser negativa.")

    return Paquetes


# Función para mostrar el vector
def Mostrar_Vector(paquetes):
    print("\nCantidades registradas:")
    for Cantidad in Paquetes:
        print(Cantidad, end=" ")
    print()


# Función para calcular el total
def Calcular_Total(Paquetes):
    return sum(Paquetes)


# Función para obtener la cantidad mayor
def Obtener_Mayor(Paquetes):
    return max(Paquetes)


# Función para contar los días con más de 20 paquetes
def Contar_Dias(Paquetes):
    Contador = 0

    for Cantidad in Paquetes:
        if Cantidad > 20:
            Contador += 1

    return Contador


# Programa principal
Paquetes = Ingresar_Paquetes()

Mostrar_Vector(Paquetes)

print("\nTotal de paquetes procesados:", Calcular_Total(Paquetes))
print("Cantidad mayor registrada:", Obtener_Mayor(Paquetes))
print("Días con más de 20 paquetes:", Contar_Dias(Paquetes))
