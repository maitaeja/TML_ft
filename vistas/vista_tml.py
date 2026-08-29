from typing import Union, List
import flet as ft
from config import COLOR_TEXTO_TITULO, COLOR_TEXTO_CUERPO

def crear_vista_tml(
    titulo: str,
    descripcion: Union[str, List[ft.TextSpan]],
    icono: ft.IconData= ft.Icons.MENU_BOOK_OUTLINED,
):
    if isinstance(descripcion, list):
        texto_control= ft.Text(
            spans=descripcion,
            size=20,
            color=COLOR_TEXTO_CUERPO,
            text_align=ft.TextAlign.JUSTIFY,
        )
    else:
        texto_control=ft.Text(
            value=descripcion,
            size=20,
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


class QueEsTMLView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = crear_vista_tml(
            "¿Qué es un TML?",

            [
                ft.TextSpan("Es un punto o área especifica designada a lo largo de un circuito de inspección (tuberías, recipientes a presión, tanques de almacenamiento, entre otros) donde se realizan inspecciones y mediciones periódicas, estas mediciones de espesor se pueden realizar mediante algún método de ensayo no destructivo, como por ejemplo:\n\n"),

                ft.TextSpan("1.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Ultrasonido Industrial (UT): es el método más común para monitorear, se usa un transductor para medir espesor de pared.\n\n"),

                ft.TextSpan("2.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Radiografía (RT): especificamente radiografía de perfil, que permite ver el espesor y posibles depósitos internos sin quitar el aislamiento térmico.\n\n"),

                ft.TextSpan("3.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Corrientes de eddy pulsadas (PEC): útil para medir espesores a través de aislamiento grueso o materiales anticorrosivos.\n\n"),

                ft.TextSpan("El concepto independiente de TML ha pasado a integrarse dentro de un término más amplio llamado CML, donde un CML puede contener uno o varios TML."),
                                
            ]            
        )

