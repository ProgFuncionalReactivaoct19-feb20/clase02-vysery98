"""
	Practica 4:

		Dada la siguiente estructura de datos

		[10, 2, 8, 7, 5, 4, 3, 11, 0, 1]

		Use:
		Función map
		Una función anónima
		que permita presentar en otra lista, cada elemento elevado a la tercera potencia.

	@vysery98
"""
lista = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]

potencia = lambda x: x ** 3

print(list(map(potencia, lista)))