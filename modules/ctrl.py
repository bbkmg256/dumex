#!/bin/env python3

# Modulo de control de Dumex

import flet as fl
import configparser as cp
import os
import subprocess as sp


# Instanciacion de configparser
config = cp.ConfigParser()
config_file="./config.INI" # Ruta de fichero de configuración


# Inicia el engiene con los parametros configurados.
def exe_all(engine, iwad):
	print(f"\n(!) Ejecutando Doom ...")
	print(f"[Info] \nEngine: {engine.value} \nIWAD: {iwad.value}\n")

	if engine.value != iwad.value and iwad.value != "":
		'''
		# Parse pwads to list
		i = 0
		lista_pwads = []
		while pwads.get(i) != "":
			lista_pwads.append(pwads.get(i))
			i += 1
		# Save config
		cad_pwads = ", ".join(lista_pwads)
		'''
		config['CFG']['engine_path'] = engine.value
		config['CFG']['iwad_path'] = iwad.value
		#config['CFG']['pwads'] = cad_pwads
		config.write(open(config_file, 'w'))
		# Execute engine with iwad
		command = [engine.value, "-iwad", iwad.value, "-file"]
		'''
		if bool(lista_pwads):
			for i in lista_pwads:
				command.append(i)
			print(command)
		'''
		sp.run(command)
	else:
		print(f"Ingrese valores validos para los campos de valores xd")

# Obtiene las rutas mediante un FileDialog.
def get_path(e: fl.FilePickerResultEvent, val_tf):
	if e.files:
		print(f"Fichero '{e.files[0].name}' seleccionado: {e.files[0].path}")
		val_tf.value = e.files[0].path
		val_tf.update()
	else: print(f"(!) No se seleccionó ningun fichero!\n")

# Verifica la existencia de un fichero de configuracion y en caso favorable, lo lee.
def verify_config(eng_tf, iwad_tf):	
	if not (os.path.exists(config_file)):
		print(f"(!) Fichero de configuración no encontrado, se ah creado uno...")
		config['CFG'] = {
			'engine_path' : '',
			'iwad_path' : '',
			'pwads': ''
			}
		config.write(open(config_file, 'w'))
	else:
		print(f"(!) Fichero de configuración encontrado...")
		config.read(config_file)
		eng_tf.value = config['CFG']['engine_path']
		iwad_tf.value = config['CFG']['iwad_path']