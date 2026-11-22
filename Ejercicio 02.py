FILAS = 2
COLUMNAS = 3

Matriz = []

# 1. Solicitar los valores y aceptar únicamente 0 o 1
for i in range(FILAS):
    Fila = []
    for j in range(COLUMNAS):
        while True:
            try:
                Valor = int(input(f"Ingrese el valor para fila {i + 1}, columna {j + 1} (0 = disponible, 1 = ocupado): "))
                if Valor in (0, 1):
                    Fila.append(Valor)
                    break
                else:
                    print("Error: solo se aceptan los valores 0 o 1.")
            except ValueError:
                print("Error: debe ingresar un número entero (0 o 1).")
    Matriz.append(Fila)

# 2. Mostrar la matriz de forma ordenada
print("\nMatriz de espacios del salón:")
for Fila in Matriz:
    print(" ".join(str(x) for x in Fila))

# 3. Contar espacios ocupados (1) y disponibles (0) en total
Ocupados_Total = sum(Fila.count(1) for Fila in Matriz)
Disponibles_Total = sum(Fila.count(0) for Fila in Matriz)

print(f"\nTotal de espacios ocupados: {Ocupados_Total}")
print(f"Total de espacios disponibles: {Disponibles_Total}")

# 4. Mostrar cuántos espacios están ocupados en cada fila
print("\nEspacios ocupados por fila:")
for i, Fila in enumerate(Matriz):
    Ocupados_Fila = Fila.count(1)
    print(f"Fila {i + 1}: {Ocupados_Fila}")
