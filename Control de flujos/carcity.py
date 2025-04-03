#Benjamin Poblete
#03-04-2025

altura = int(input("¿Cual es tu altura (cm)?"))
#Crearon una variable para solicitar informacion al usuario
creditos = int(input("¿Cuantos creditos tienes?"))

if altura >= 137 and creditos >=10:
    print('Disfruta tu viaje')
    
elif altura < 137 and creditos >=10:
    print("No tienes suficiente credito")
    
else:
    print("no tienes altura ni los creditos necesarios para subir")