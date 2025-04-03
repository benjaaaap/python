#Benjamin Poblete
#Tengo casi 18
#02-04-2025

respuesta = input("¿estas cansado? (sí/no)").strip().lower()

cansado = respuesta == "sí"

if not cansado: 
    print("!Es hora de programar")
    
else: print("tomate un descanso, lo necesitas")