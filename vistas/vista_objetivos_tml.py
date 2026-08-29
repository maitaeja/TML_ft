from typing import Union, List
import flet as ft
from config import COLOR_TEXTO_TITULO, COLOR_TEXTO_CUERPO

def crear_vista_objtml(
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

            ft.Column(
                controls=[
                    ft.Container(
                        content= texto_control,
                        padding=ft.Padding.only(left=40, right=40)
                    )
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            ),
        ],
        spacing=20,
        expand=True,
    )


class ObjetivosTMLView(ft.Container):
    def __init__(self):
        super().__init__(expand = True)
        self.content = crear_vista_objtml(
            "Objetivos de los TML's",

            [
                ft.TextSpan("Objetivo general:\n\n", ft.TextStyle(weight=ft.FontWeight.BOLD, size=25)),
                ft.TextSpan("Garantizar que las áreas con mayor probabilidad de degradación sean monitoreadas de manera consistente a lo largo del ciclo de vida del activo..\n\n"),
                            
                ft.TextSpan("Objetivos específicos:\n\n", ft.TextStyle(weight=ft.FontWeight.BOLD, size=25)),
                ft.TextSpan("Los TML´s son de vital importancia para:\n"),
                                      
                ft.TextSpan("1.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Detectar pérdida de espesor.\n"),
                                        
                ft.TextSpan("2.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Monitorear y evaluar la integridad mecánica de los activos de una planta industrial (tuberías, recipientes a presión, tanques de almacenamiento, entre otros) a lo largo del tiempo.\n"),
                           
                ft.TextSpan("3.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Calcular velocidad de corrosión.\n"),
                           
                ft.TextSpan("4.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Estimar vida útil remanente del componente.\n"),
                            
                ft.TextSpan("5.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" Cumplimiento normativo: estándares internacionales como API 510/API 570 exigen el establecimiento de circuitos de inspección basados en TML's."),
            ]
            
        )

            
