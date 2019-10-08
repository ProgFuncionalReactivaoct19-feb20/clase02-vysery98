"""
	Practica 2:

		Desarrollar una función anónima que permita retornar la siguiente salida, ejemplo:

		CUENCA capital de AZUAY

		La llamada a la función es

		print(cadena_personalizada("Cuenca", "Azuay"))

	@vysery98
"""

# Funcion anonima recibe dos valores x (Cuenca) - y (Azuay)
cadena_personalizada = lambda x, y: ("%s capital de %s" % (x.upper(), y.upper()))

# Se envía a la función anónima cadena_personalizada valores y se imprime según las indicaciones dadas a la función
print(cadena_personalizada("Cuenca", "Azuay"))