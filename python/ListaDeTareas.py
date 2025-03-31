tareas = ['🏦 Sacar dinero del banco.',
          '🫗Hacer la colada',
          '🪴Dar un paseo.',
          '💈Cortarse el cabello.',
          '☕ Preparar un té.',
          '💻 Terminar el capitulo de Listas.',
          '♥️ Llamar a mamá.',
          '📺 Ver mi Hero Academia.']

#1 Acceder a la primera tarea de la lista
print(tareas[0])

#2 Encontrar la segunda tarea de la lista
print(tareas[1])

#3 Obtener un subconjunto de tareas usando slicing (rebanado)
print(tareas[2:3])

#4 Intentar acceder a un indice inexistente y manejar el error
indice = 8
try:
    print(tareas[indice])
    
except IndexError:
    print('Lamentablemente no encontramos tu tarea:( ')

#5 Nueva tarea
nueva_tarea = '📚estudiar'

# Agrega 'nueva_tarea' al final de 'tareas'
tareas = tareas + [nueva_tarea]  
print(tareas)