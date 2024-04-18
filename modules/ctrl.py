#!/bin/env python3


# LIBS.
import configparser as cp
import os
import subprocess as sp
import tkinter
from tkinter import filedialog


# Control class
class CTRL:
	# Construct. #
	def __init__(self):
		# Config atribute
		self._config = cp.ConfigParser()
		self._config_file_path = None


	# Getters #
	def get_config(self):
		return self._config['CFG']

	def get_engine_path(self):
		return self._config['CFG']['engine_path']

	def get_iwad_path(self):
		return self._config['CFG']['iwad_path']

	def get_pwads(self):
		pass


	# Methods. #
	# Config verify-creation (.INI)
	def verify_config(self, config_file, ):
		self._config_file_path = config_file
		# Verify that the config file exists
		if not (os.path.exists(config_file)):
			self._config['CFG'] = {
				'engine_path' : '',
				'iwad_path' : '',
				'pwads': ''
			}
			self._config.write(open(config_file, 'w'))
			print(f"Fichero de configuración no encontrado, se ah creado uno...")
		else:
			self._config.read(config_file)
			print(f"Fichero de configuración encontrado...")

	# "Search file" method
	def search_file(self, box):
		if isinstance(box, tkinter.Entry):
			if box.get() != "":
				box.delete(0, tkinter.END)
			box.insert(0, tkinter.filedialog.askopenfilename())
		else:	
			box.insert(tkinter.END, tkinter.filedialog.askopenfilename())

	# "Execute all" method
	def exe(self, engine_path, iwad_path, pwads):
		if engine_path != iwad_path and iwad_path != "":
			# Parse pwads to list
			i = 0
			lista_pwads = []
			while pwads.get(i) != "":
				lista_pwads.append(pwads.get(i))
				i += 1
			# Save config
			cad_pwads = ", ".join(lista_pwads)
			self._config['CFG']['engine_path'] = engine_path
			self._config['CFG']['iwad_path'] = iwad_path
			self._config['CFG']['pwads'] = cad_pwads
			self._config.write(open(self._config_file_path, 'w'))
			# Execute engine with iwad
			command = [engine_path, "-iwad", iwad_path, "-file"]
			if bool(lista_pwads):
				for i in lista_pwads:
					command.append(i)
				print(command)
			sp.run(command)
		else:
			print(f"Ingrese valores validos para los campos de valores xd")
