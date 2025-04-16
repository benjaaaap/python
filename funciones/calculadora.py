#Benjamin Poblete
#16/04/2025
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def potencia(a, b):
    return a ** b

# Ejemplo de uso
if __name__ == "__main__":
    print("Suma:", sumar(4, 4))
    print("Resta:", restar(8, 4))
    print("Multiplicación:", multiplicar(5, 2))
    print("División:", dividir(10, 5))
    print("Potencia:", potencia(2, 3))