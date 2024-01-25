""" Práctica Módulo Collections 2
Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, se cargue con el string "Valor no hallado".
Carga el diccionario, al menos, con el siguiente par de datos:
palabra clave = edad
valor = 44
Utiliza el método defaultdict del módulo Collections. """

from collections import defaultdict


mi_diccionario = defaultdict(lambda: "Valor no hallado")

mi_diccionario['palabra_clave'] = "edad"
mi_diccionario['valor'] = 44
print(mi_diccionario['palabra_clave'], mi_diccionario['valor'])#imprime edad 44





