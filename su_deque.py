
""" 
Práctica Módulo Collections 3
Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de datos lineal que permite insertar y eliminar elementos por ambos extremos.
Investiga más al respecto en cualquier sitio de documentación, y a continuación implementa una deque a partir del módulo collections. Los elementos iniciales de la lista se brindan a continuación.
["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.
"""
from collections import deque

# Lista inicial
lista_ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

# Convertir la lista en un deque
deque_ciudades = deque(lista_ciudades)

# Incorporar un elemento por la izquierda
deque_ciudades.appendleft("Nueva York")

# Imprimir la deque resultante
print(deque_ciudades)
