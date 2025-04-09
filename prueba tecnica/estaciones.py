#Benjamin Poblete
#09-04-2025
#tengo la mejor extencion de todo vscode UwU

mes = int(input("Ingrese el número del mes (1-12): ")) #Le pediremos al usuario que ingrese el numero del mes con input y int porque ingresara un numero


if mes in [1, 2, 3]:      # En los meses de enero, febrero y marzo nos debera imprimir invierno
    print("Invierno")
elif mes in [4, 5, 6]:    # En los meses de abril, mayo y junio nos debera imprimir primavera
    print("Primavera")
elif mes in [7, 8, 9]:    # En los meses de julio, agosto y septiembre nos debera imprimir verano
    print("Verano")
elif mes in [10, 11, 12]: # En los meses de octubre, noviembre y diciembre nos debera imprimir otoño
    print("Otoño")
else:
    print("Invalid")      # Si ingresamos un numero que no corresponde a ningun mes nos imprimira "Invalid"