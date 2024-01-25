from collections import Counter, defaultdict, namedtuple

""" numeros = [6,5,4,6,4,3,2,2,2,2,5,6,7,9,1,]
print(Counter(numeros)) """


""" mi_dic = defaultdict(lambda: "nada")
mi_dic['uno'] = 'Verde'
print(mi_dic['dos']) #Como 'dos' no existe imprime nada """


""" Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
#creo una instancia de persona
ariel = Persona('Ariel',1.76,79)
print(ariel.nombre, ariel.peso)
 """

#Con este codigo imprime Nombre: ariel, Peso:79
from collections import namedtuple

# Defino la namedtuple Persona con campos: nombre, altura y peso
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
# Creo una instancia de Persona llamada ariel
ariel = Persona('Ariel', 1.76, 79)
# Imprimo en formato deseado
print(f"Nombre: {ariel.nombre},\n Altura: {1.76},\n Peso: {ariel.peso}")




