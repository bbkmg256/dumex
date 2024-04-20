#!/bin/env python3

# Modulo de interfaz de Dumex (apoyado en flet framework)

import flet as fl
from . import ctrl


# Prod. principal de UI
def main_ui(page: fl.Page):
    # Definición de valores y catacteristicas
    page.title = "Dumex"
    page.window_width, page.window_height = 1000, 500
    #page.window_resizable = False # No funciona bien en linux
    page.update()

    engine_tf = fl.TextField(label="Ruta del Engine (GZDOOM)")
    iwad_tf = fl.TextField(label="Ruta del .IWAD")
    # pwad = ...

    # Verifica configuracion
    ctrl.verify_config(eng_tf=engine_tf, iwad_tf=iwad_tf)
    
    # FileDialog para Engine
    picker_fd_engine = fl.FilePicker(on_result=lambda e: ctrl.get_path(e, val_tf=engine_tf)); page.overlay.append(picker_fd_engine)
    bt_picker_fd_engine = fl.ElevatedButton(text="Buscar Engine", on_click=lambda _: picker_fd_engine.pick_files(allow_multiple=False))
   
    # FileDialog para IWAD
    picker_fd_iwad = fl.FilePicker(on_result=lambda e: ctrl.get_path(e, val_tf=iwad_tf)); page.overlay.append(picker_fd_iwad)
    bt_picker_fd_iwad = fl.ElevatedButton(text="Buscar IWAD", on_click=lambda _: picker_fd_iwad.pick_files(allow_multiple=False))

    # Boton Iniciar xd
    bt_start = fl.ElevatedButton(text="INICIAR", on_click=lambda _: ctrl.exe_all(engine=engine_tf, iwad=iwad_tf))

    # Añadiendo los widgets a la ventana
    page.add(
        # Organizacion en Columnas
        fl.Column([
            # Organizacion en Filas
            fl.Row([
                engine_tf, bt_picker_fd_engine
            ]),
            fl.Row([
                iwad_tf, bt_picker_fd_iwad
            ]),
            bt_start
        ])
    )