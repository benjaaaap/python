adivinanza = 0 
intentos = 0
max_intentos= 3


while adivinanza !=6 and intentos < max_intentos:
    adivinanza = int(input("Adivina el número:"))
    intentos +=1
    
    
if adivinanza ==6:
    print("Muy bien adivinaste!!")
    
    
    
else:
    print("Se acabaron los intentos. ¡Mejor suerte la próxima vez!")