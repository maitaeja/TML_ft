import flet as ft
from formulario.form_maestro_desing import FormularioMaestroDesing
import os
import ssl
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA



# Arreglo para el error de certificados (SSL)
try:
    ssl._create_default_https_context = ssl._create_unverified_context
except AttributeError:
    pass
#------------------------------------------------------------------------------


def main(page: ft.Page):
    page.title = "Integridad y Corrosión"
    page.padding = 0
    page.spacing = 0

    formulario = FormularioMaestroDesing(page)

    def on_resize(e):
        # Validar que page.width no sea None y aplicar responsividad
        ancho = page.width if page.width is not None else 1000
        if hasattr(formulario, "barra_lateral_i"):
            formulario.barra_lateral_i.visible = (ancho >= 768)
            page.update()

    page.on_resize = on_resize
    page.add(formulario)

# Obtener puerto configurado por Render o usar 8080 por defecto
port = int(os.environ.get("PORT", 8080))

ft.app(
    target=main,
    assets_dir="imagenes",
    view=ft.AppView.WEB_BROWSER,
    host="0.0.0.0",
    port=port
)