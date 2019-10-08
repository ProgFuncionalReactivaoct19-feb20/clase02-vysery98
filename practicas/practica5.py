"""
	Practica 5:

		Dada la siguiente estructura de datos

		[(10,2), (8,7), (5,4), (3,11), (10,11)]

		Use:
		Función map
		Dos funciones anónimas
		que permita presentar en otra lista; para las primeras posiciones la raiz cuadrada, para las segundas posiciones el cuadrado del número

	@vysery98
"""

# Importacion de paquete para usar .sqrt y .pow
import math

lista = [(10,2), (8,7), (5,4), (3,11), (10,11)]

# Operaciones de raiz y potencia en funciones lambda
raiz = lambda x: math.sqrt(x[0])
potencia = lambda x: math.pow(x[1], 2)

# Envio de datos a funciones por medio de otra funcion lambda
presentacion = lambda x: (raiz(x), potencia(x))

# Salida de la lista
print(list(map(presentacion, lista)))