#!/bin/env python3

# Dumex (v0.2.0)
# Un front-end para GZDoom :)

import flet as fl
from modules import ui


# Condición de ejecucion principal
if __name__ == '__main__':
	print(f"(!) Iniciando Dumex...")
	fl.app(ui.main_ui)
	print(f"(!) Adiós :)\n")