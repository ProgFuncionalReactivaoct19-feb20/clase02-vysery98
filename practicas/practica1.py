"""
	Practica 1: 

		Desarrollar la función anónima que retorne True or False si el número dado es par.
	
		Ejemplo de llamada

		print(valor_par(2))
		print(valor_par(3))
		print(valor_par(11))

	@vysery98
"""

# Ingreso de dato a analizar
num = int(input("Ingrese un valor numérico: "))

# Funcion lambda(anonima) que divide el valor ingresado para dos y compara si el resultado es igual a 0
valor_par = lambda x: x % 2 == 0

# Devuelve el valor de True o False dependiendo de la comparacion del valor ingresado para 2
print(valor_par(num))
