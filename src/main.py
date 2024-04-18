#!/bin/env python3


# Dumex win-ver (v0.1.0)

# Frontend para ejecutar Gzdoom con mods

'''
NOTA:

	Cosas por hacer:
		- Mejorar la interfaz (es decir las disposicion de todos los widgets)
		- Contemplar fallos al intentar ejecutar comandos con rutas no validas

	Cosas solucionadas o hechas:
		- Mejorar codigo y pasarlo a POO (solucionado, bueno mejorar el codigo, todavia no)
		- Agregar integracion para la ejecucion de mods (Listo)
		- Agregar una listbox para visualizar todos los mods cargados (Listo)


	Porcion de codigo útil:
		engine = "D:/gzdoom/gzdoom"
		iwad = "D:/gzdoom/IWAD/DOOM2.WAD"
		pwads = ["D:/gzdoom/PWAD/bd64game_v2.5.pk3", "D:/gzdoom/PWAD/bd64maps_v2.5.pk3"]
		comando = [engine, "-iwad", iwad, "-file"]
		for i in pwads:
			comando.append(i)

		print(f"{comando}")
		sp.run(comando)
'''


# LIBS.
from src import iu


# Main class
class Main:
	# Construct. #
	def __init__(self):
		pass
	

	# Methods. #
	def run(self):
		print(f"Iniciando Dumex...")
		window = iu.IU(title="Dumex", geometry="500x300", resizable=[False, False])
		window.display_iu()


main = Main()
main.run()