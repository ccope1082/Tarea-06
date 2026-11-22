def main():
    Unidades_Caja = 12

    # Solicita los artículos a empacar
    Articulos = int(input("Ingrese el total de artículos: "))

    # Validar que la cantidad digitada no sea negativa
    if Articulos < 0:
        print("Error: La cantidad de artículos no puede ser negativa.")
    else:
        # Calcula las cajas completas
        Cajas_llenas = Articulos // Unidades_Caja

        # Calcula los artículos sobrantes
        Sobrantes = Articulos % Unidades_Caja

        # Calcula los artículos faltantes para completar otra caja
        if Sobrantes > 0:
            Sin_Empacar = Unidades_Caja - Sobrantes
        else:
            Sin_Empacar = 0

        # Muestra los resultados al usuario
        print("\n--- Resultados ---\n")
        print(f"Cajas completas: {Cajas_llenas}")
        print(f"Artículos sin empacar: {Sobrantes}")

        if Sobrantes > 0:
            print(f"Se requieren {Sin_Empacar} artículos para completar otra caja.")
        else:
            print("No sobran artículos, todas las cajas están completas.")


if __name__ == "__main__":
    main()
