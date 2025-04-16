#Benjamin Poblete
#16/04/2025


def kilometros_a_millas(kilometros):
    # 1 milla equivale a 1.609 kilómetros
    millas = kilometros / 1.609
    return millas

def distancia_a_millas(distancia):
    # 1 kilómetro equivale a aproximadamente 0.621371 millas
    millas = distancia * 0.621371
    return millas

# Llamar a la función con 10000 kilómetros
resultado = distancia_a_millas(10000)
print(f"10000 kilómetros son aproximadamente {resultado} millas.")