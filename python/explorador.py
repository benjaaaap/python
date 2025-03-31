#Benjamin Poblete
#soy programador y tengo 17 años
#17/03/2025

#crear lista

mi_lista = [1, 2, 3, 4, 5]

#1 Muestra el tercer elemento de la lista
print(mi_lista[3])

#2 Cambia el valor del ultimo elemento
mi_lista[-1]=10
print(mi_lista)

#3 Agregar un nuevo elemento al final de la lista
mi_lista.append(60)
print(mi_lista)

#4 Insertar un elemento en la segunda posicion de la lista
mi_lista[1] = 55
print(mi_lista)

#5 Elimina un elemento de la lista usando su valor
eliminado = mi_lista.pop(5)
print(mi_lista)

#6 Encuentra la posicion de un elemento especifico con .index()
indice = mi_lista.index(3)
print(indice)

#7. Ordena la lista alfabeticamente de menor a mayor si son numeros.
mi_lista.sort()
print(mi_lista)

#8 Invierte el orden de la lista
mi_lista.reverse()
print(mi_lista)