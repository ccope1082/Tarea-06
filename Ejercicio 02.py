FILAS = 2
COLUMNAS = 3

matriz = []

# 1. Solicitar los valores y aceptar únicamente 0 o 1
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        while True:
            try:
                valor = int(input(f"Ingrese el valor para fila {i + 1}, columna {j + 1} (0 = disponible, 1 = ocupado): "))
                if valor in (0, 1):
                    fila.append(valor)
                    break
                else:
                    print("Error: solo se aceptan los valores 0 o 1.")
            except ValueError:
                print("Error: debe ingresar un número entero (0 o 1).")
    matriz.append(fila)

# 2. Mostrar la matriz de forma ordenada
print("\nMatriz de espacios del salón:")
for fila in matriz:
    print(" ".join(str(x) for x in fila))

# 3. Contar espacios ocupados (1) y disponibles (0) en total
ocupados_total = sum(fila.count(1) for fila in matriz)
disponibles_total = sum(fila.count(0) for fila in matriz)

print(f"\nTotal de espacios ocupados: {ocupados_total}")
print(f"Total de espacios disponibles: {disponibles_total}")

# 4. Mostrar cuántos espacios están ocupados en cada fila
print("\nEspacios ocupados por fila:")
for i, fila in enumerate(matriz):
    ocupados_fila = fila.count(1)
    print(f"Fila {i + 1}: {ocupados_fila}")
