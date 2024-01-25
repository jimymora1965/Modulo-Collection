from collections import deque

lista_profesiones = ["Médico", "Abogado", "Chofer"]

#convierto la lista en un deque
deque_profesiones = deque(lista_profesiones)

deque_profesiones.append("Desarrollador")#deque por la derecha
print(deque_profesiones)

deque_profesiones.appendleft("Escritor")#deque por la izquierda
print(deque_profesiones)
