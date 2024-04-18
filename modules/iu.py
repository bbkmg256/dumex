#!/bin/env python3


# LIBS.
import tkinter as tk
from . import ctrl


# User Interfaces class
class IU:
	# Construct. #
	def __init__(self, title, geometry, resizable):
		# Atributes for window
		self._root = tk.Tk()
		self._title = title
		self._geometry = geometry
		self._resizable = resizable

		# Atributes for widgets
		self._engine_tb = None
		self._iwad_tb = None
		self._pwad_lb = None

		# Atributes for controls
		self._control = ctrl.CTRL()
		self._engine_data = None # config['CFG']['engine_path']
		self._iwad_data = None # config['CFG']['iwad_path']
		self._pwad_data = None


	# Methods. #
	# Visualization metod
	def display_iu(self):
		# Config verify
		self._control.verify_config('./config.ini')

		# Set window tk config
		self._root.title(self._title)
		self._root.geometry(self._geometry)
		self._root.resizable(self._resizable[0], self._resizable[1])

		# Text tags
		# ENGINE tag
		tk.Label(self._root, text="ENGINE path..").grid(column=0, row=0)
		# IWAD tag
		tk.Label(self._root, text="IWAD path..").grid(column=0, row=2)
		# PWAD tag
		tk.Label(self._root, text="PWADs path..").grid(column=3, row=0)

		# Text-boxes
		# ENGINE entry
		self._engine_tb = tk.Entry(self._root)
		self._engine_tb.grid(column=0, row=1) 
		self._engine_tb.insert(0, self._control.get_engine_path())
		# IWAD entry
		self._iwad_tb = tk.Entry(self._root)
		self._iwad_tb.grid(column=0, row=3)
		self._iwad_tb.insert(0, self._control.get_iwad_path())

		# List box
		# PWAD L-B
		self._pwad_lb = tk.Listbox(self._root)
		self._pwad_lb.grid(column=3, row=1)

		# Buttons
		# Search engine button
		tk.Button(self._root, text="...", command=lambda : self._control.search_file(self._engine_tb)).grid(column=2, row=1)
		# Search iwad button
		tk.Button(self._root, text="...", command=lambda : self._control.search_file(self._iwad_tb)).grid(column=2, row=3)
		# Search-add pwads button
		tk.Button(self._root, text="Agregar", command=lambda : self._control.search_file(self._pwad_lb)).grid(column=3, row=2)
		# Delete pwad button
		#tk.Button(self._root, text="Eliminar", command=None)

		# Run engine, iwad and pwads
		tk.Button(self._root, text="Iniciar", command=lambda : self._control.exe(engine_path=self._engine_tb.get(), iwad_path=self._iwad_tb.get(), pwads=self._pwad_lb)).grid(column=0, row=6)
		
		# Loop for window tk
		self._root.mainloop()
