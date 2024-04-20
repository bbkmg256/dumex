#!/bin/env python3

# Modulo de interfaz de Dumex (apoyado en flet framework)

import flet as fl
from . import ctrl


# Prod. principal de UI
def main_ui(page: fl.Page):
    # Definición de valores y catacteristicas
    page.title = "Dumex"
    page.window_width, page.window_height = 500, 300
    #page.window_resizable = False # No funciona bien en linux
    page.update()

    engine_tf = fl.TextField(label="Ruta del Engine (GZDOOM)")
    iwad_tf = fl.TextField(label="Ruta del .IWAD")
    pwad_tf = fl.TextField(label="Ruta dir. Mods")

    # Verifica configuracion
    ctrl.verify_config(eng_tf=engine_tf, iwad_tf=iwad_tf, pwads_tf=pwad_tf)
    
    # FileDialog para Engine
    picker_fd_engine = fl.FilePicker(on_result=lambda e: ctrl.get_path(e, val_tf=engine_tf, directory=False)); page.overlay.append(picker_fd_engine)
    bt_picker_fd_engine = fl.ElevatedButton(text="Buscar Engine", on_click=lambda _: picker_fd_engine.pick_files(allow_multiple=False))
   
    # FileDialog para IWAD
    picker_fd_iwad = fl.FilePicker(on_result=lambda e: ctrl.get_path(e, val_tf=iwad_tf, directory=False)); page.overlay.append(picker_fd_iwad)
    bt_picker_fd_iwad = fl.ElevatedButton(text="Buscar IWAD", on_click=lambda _: picker_fd_iwad.pick_files(allow_multiple=False))

    # FileDialog para PWADs
    picker_fd_pwad = fl.FilePicker(on_result=lambda e: ctrl.get_path(e, val_tf=pwad_tf, directory=True)); page.overlay.append(picker_fd_pwad)
    bt_picker_fd_pwad = fl.ElevatedButton(text="Buscar dir. Mods", on_click=lambda _: picker_fd_pwad.get_directory_path())

    # Boton Iniciar xd
    bt_start = fl.ElevatedButton(text="INICIAR", on_click=lambda _: ctrl.exe_all(engine=engine_tf, iwad=iwad_tf, pwads=pwad_tf))

    # Boton Limpiar todo xd
    bt_clean = fl.ElevatedButton(text="Limpiar", on_click=lambda _: ctrl.clean(engine=engine_tf, iwad=iwad_tf, pwads=pwad_tf))

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
            fl.Row([
                pwad_tf, bt_picker_fd_pwad
            ]),
            fl.Row([
                bt_start,
                bt_clean
            ])
        ])
    )