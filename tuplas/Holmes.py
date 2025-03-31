pistas = ( "Puerta Roja", 221, "Londres", 3.14, "Watson", 7, "Moriarty" )

print("🔎 !Bienvenido, detective Holmes!")
print("📃 Se ha encontrado una serie de pistas misteriosas...")
print("🗝️ Pistas encontradas:", pistas)

# 📌 Analisis de pistas
print("\n🕵️ Analizando las pistas...")

#1 Primera pista
print(pistas[0])

#2 Ultima pista
print(pistas[-1])

#3 Total de pistas
print(len(pistas))

#4 Esta londres en las pistas?
print("Londres" in pistas)

#5 Desempaqueta las primera tres pistas 


#6 Crear tupla con mas pistas
tupla2 = ("Sherlock", 512, "Holmes")

#7 Encuentra la posicion de "Watson"
print(pistas.index("Watson"))

#8 Cuantas veces aparece el numero 7 en las pistas?
print(pistas.count(7))

print ("\n🕵️ Felicitaciones, detective. !Has resuelto el analisis inicial de las pistas!")
print ("🔐 Ahora, sigue con las deducciones para resolver el misterio")