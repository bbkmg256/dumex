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
def exe_all(engine, iwad, pwads):
	print(f"\n(!) Ejecutando Doom ...")
	print(f"[Info] \nEngine: {engine.value} \nIWAD: {iwad.value} \nMods dir.: {pwads.value}\n")

	#if engine.value != iwad.value and iwad.value != "":
	if engine.value != iwad.value and iwad.value != pwads.value and pwads.value != "":
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
		config['CFG']['pwads'] = pwads.value
		config.write(open(config_file, 'w'))
		# Execute engine with iwad
		command = [engine.value, "-iwad", iwad.value, "-file", f"{pwads.value}/*"]
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
def get_path(e: fl.FilePickerResultEvent, val_tf, directory):
	if directory:
		# Directorio
		if e.path:
			print(f"(!) Seleccionado dir.: {e.path}")
			val_tf.value = e.path
			val_tf.update()
		else: print(f"(!) No se seleccionó ningun directorio!\n")
	else:
		# Fichero
		if e.files:
			print(f"(!) Seleccionado fichero: {e.files[0].path}")
			val_tf.value = e.files[0].path
			val_tf.update()
		else: print(f"(!) No se seleccionó ningun fichero!\n")

# Verifica la existencia de un fichero de configuracion y en caso favorable, lo lee.
def verify_config(eng_tf, iwad_tf, pwads_tf):	
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
		pwads_tf.value = config['CFG']['pwads']

def clean(engine, iwad, pwads):
	engine.value, iwad.value, pwads.value = "", "", ""
	engine.update(); iwad.update(); pwads.update()
	print(f"(!) Campos limpiados!\n")