"""
	Ejemplo 1: uso de función lambda
	@vysery98
"""

lista = [10, 2, 3, 5]

print(min(lista, key=lambda x: x+100))
