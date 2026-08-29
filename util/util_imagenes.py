import flet as ft

def leer_imagen(path, size):
    return ft.Image(
        src=path,
        width=ancho,
        height=alto,
        fit=ft.Image.Fit.CONTAIN

    )