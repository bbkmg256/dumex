#!/bin/env python3


# Dumex (v0.1.0)
# Frontend para ejecutar Gzdoom con mods


# LIBS.
from modules import iu


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
