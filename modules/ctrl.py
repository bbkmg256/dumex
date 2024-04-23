#!/bin/env python3

# Modulo de control de Dumex

import flet as fl
import configparser as cp
import os
import subprocess as sp


# Obtine el nombre del usuario del sistema
user_name = sp.run(["whoami"], capture_output=True, text=True)
# Instanciación de configparser
config = cp.ConfigParser(); cf_name = 'dumex_conf.INI'


# Definición de ruta de fichero
def os_reco():
	global cf_path
	if os.name == "nt":
		cf_path = f'C:\\Documents\\dumex\\{cf_name}'.replace ("\n", "") # Win
		print(f"(!) Entorno encontrado: Windows\n")
	elif os.name == "posix":
		cf_path = f'/home/{user_name.stdout}/.config/dumex/{cf_name}'.replace ("\n", "") # Unix
		print(f"(!) Entorno encontrado: Unix\n")
	else:
		# Forma de manejar el fichero en S.O raros xd
		cf_path = f"./{cf_name}"
		print(f"(!) OS no identificado!\n")

# Inicia el engine con los parametros configurados.
def exe_all(engine, iwad, pwads, pwads_cb):
	# Almacenando cfg
	config['CFG']['engine_path'] = engine.value
	config['CFG']['iwad_path'] = iwad.value
	config['CFG']['pwads'] = pwads.value
	config['CFG']['mods_enable'] = str(pwads_cb.value)
	config.write(open(cf_path, 'w'))
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
	# Si, ya sé que esto no está bien, es momentaneo
	if not pwads.disabled:
		if engine.value != iwad.value != pwads.value != "":
			print(f"\n(!) Ejecutando Doom con mods ...")
			print(f"[Info] \nEngine: {engine.value} \nIWAD: {iwad.value} \nMods dir.: {pwads.value}\n")
			
			# lista para el comando a ejecutar
			command = [engine.value, "-iwad", iwad.value, "-file", f"{pwads.value}/*"]
			'''
			if bool(lista_pwads):
				for i in lista_pwads:
					command.append(i)
				print(command)
			'''
			sp.run(command)
		else:
			print(f"(!) Ingrese valores validos para los campos de valores xd")
	else:
		if engine.value != iwad.value != "":
			print(f"\n(!) Ejecutando Doom sin mods ...")
			print(f"[Info] \nEngine: {engine.value} \nIWAD: {iwad.value}\n")
			
			config['CFG']['engine_path'], config['CFG']['iwad_path'] = engine.value, iwad.value
			config.write(open(cf_path, 'w'))
			# lista para el comando a ejecutar
			command = [engine.value, "-iwad", iwad.value]
			sp.run(command)
		else:
			print(f"(!) Ingrese valores validos para los campos de valores xd")

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

# Verifica la la configuración.
def verify_config(eng_tf, iwad_tf, pwads_tf, pwads_bt, pwads_cb):
	os_reco() # Reconocimiento de S.O
	# Comprueba existencia de directorio
	if not (os.path.exists(cf_path[:len(cf_path) - (len(cf_name)+1)])):
		print(f"(!) No se encontro directorio de configuración, se ah creado uno...")
		# Crea dir.
		sp.run(["mkdir", f"{cf_path[:len(cf_path) - (len(cf_name)+1)]}"])
	# comprueba existencia de fichero
	if not (os.path.exists(cf_path)):
		print(f"(!) Fichero de configuración no encontrado, se ah creado uno...")
		# Escribe fichero
		config['CFG'] = {
			'engine_path' : '',
			'iwad_path' : '',
			'pwads': '',
			'mods_enable': 'False'
			}
		config.write(open(cf_path, 'w'))
	else:
		print(f"(!) Fichero de configuración encontrado...")
		# Lee fichero
		config.read(cf_path)
		# Campo texto
		eng_tf.value = config['CFG']['engine_path']
		iwad_tf.value = config['CFG']['iwad_path']
		pwads_tf.value = config['CFG']['pwads']
		
		# Verificacion de habilitacion comp
		pwads_tf.disabled = not eval(config['CFG']['mods_enable'])
		pwads_bt.disabled = not eval(config['CFG']['mods_enable'])
		pwads_cb.value = eval(config['CFG']['mods_enable'])
		#pwads_tf.update(); pwads_bt.update(); pwads_cb.update()

# Limpia los campos de texto
def clean(engine, iwad, pwads):
	engine.value, iwad.value, pwads.value = "", "", ""
	engine.update(); iwad.update(); pwads.update()
	print(f"(!) Campos limpiados!\n")

# Deshabilita componente
def disable_comp(*args):
	print(f"(!) Mods: {args[0].disabled}\n")
	for comp in args:
		comp.disabled = not comp.disabled
		comp.update()