from typing import Union, List
import flet as ft
from config import COLOR_TEXTO_TITULO, COLOR_TEXTO_CUERPO

def crear_vista_defpunto(
    titulo: str,
    descripcion: Union[str, List[ft.TextSpan]],
    icono: ft.IconData= ft.Icons.MENU_BOOK_OUTLINED,
):
    if isinstance(descripcion, list):
        texto_control= ft.Text(
            spans=descripcion,
            size=25,
            color=COLOR_TEXTO_CUERPO,
            text_align=ft.TextAlign.JUSTIFY,
        )
    else:
        texto_control=ft.Text(
            value=descripcion,
            size=25,
            color=COLOR_TEXTO_CUERPO,
            text_align=ft.TextAlign.JUSTIFY,
        )
                             
    
    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(
                            icono,
                            color=ft.Colors.BLUE_700,
                            size=28,
                        ),
                        bgcolor=ft.Colors.BLUE_50,
                        padding=ft.Padding.all(10),
                        border_radius=ft.BorderRadius.only(top_right=8, bottom_right=8),
                        border=ft.Border.only(left=ft.BorderSide(width=4, color=ft.Colors.BLUE_600)
                        ),
                            ),
                    ft.Text(
                        value=titulo,
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=COLOR_TEXTO_TITULO,
                        #text_align=ft.TextAlign.CENTER,
                        width=float("inf")
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
            ),
                
            ft.Divider(height=10, color=COLOR_TEXTO_TITULO),
    
            ft.Container(
                content= texto_control,
                padding=ft.Padding.only(left=40, right=40)
            )
        ],
        spacing=20,
    )


class RegistroTmlView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = crear_vista_defpunto(
            "Definición de punto",
            [
                ft.TextSpan("Antes de comprender el concepto de TML, es importante precisar qué se entiende por"),                     
                ft.TextSpan(" \"punto\" ", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan("desde el punto de vista matemático, ya que este término constituye la base para comprender todo lo referente a la ubicación precisa donde se efectúan las mediciones de espesor.\n"),
                ft.TextSpan("El punto  se  puede definir como:\n\n"),

                ft.TextSpan("1.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Lugar  geométrico  que  define una posición  exacta en el  espacio.\n\n"),

                ft.TextSpan("2.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Adimensional, no posee longitud/ancho/altura.\n\n"),

                ft.TextSpan("3.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Producto de la intersección de dos rectas.\n\n"),
            ]
        )

        

