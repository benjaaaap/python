import random

def fortuna():
    opciones = [
        "No persigas la felicidad, creala.",
        "Todas las cosas son dificiles antes de ser faciles.",
        "El pajaro madrugador consigue el gusano, pero el segundo raton se lleva el queso.",
        "Alguien en tu vida necesita una carta de tu parte.",
        "No solo pienses. ¡Actua!",
        "Tu corazon se acelerará.",
        "La fortuna que buscas esta en otra galleta.",
        "¡Ayuda! ¡Estoy prisioneroen una panadería china!",
    ]
    
    fortuna = random.choice(opciones)
    print(f"Tu fortuna es: {fortuna}")

fortuna()