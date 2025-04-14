#benjamin poblete
# 09-04-2025

def main():

    peso_tierra = float(input("Ingrese su peso en la Tierra (en kg): "))


    print("Seleccione el número del planeta al que desea convertir su peso:")
    print("1. Mercurio")
    print("2. Venus")
    print("3. Marte")
    print("4. Júpiter")
    print("5. Saturno")
    print("6. Urano")
    print("7. Neptuno")
    planeta = int(input("Ingrese el número del planeta: "))


    gravedades = {
        1: 0.38,  # Mercurio
        2: 0.91,  # Venus
        3: 0.38,  # Marte
        4: 2.53,  # Júpiter
        5: 1.07,  # Saturno
        6: 0.89,  # Urano
        7: 1.14   # Neptuno
    }


    if planeta in gravedades:
        peso_destino = peso_tierra * gravedades[planeta]
        print(f"Su peso en el planeta seleccionado es: {peso_destino:.2f} kg")
    else:
        print("Número de planeta no válido. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()