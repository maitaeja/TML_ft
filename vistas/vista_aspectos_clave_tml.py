from typing import Union, List
import flet as ft
from config import COLOR_TEXTO_TITULO, COLOR_TEXTO_CUERPO

def crear_vista_aspectos(
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



class AspectosClaveView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = crear_vista_aspectos(
            "Aspectos clave de los TML's",
            
            [
            ft.TextSpan("Para que la información recopilada en campo sea útil para la toma de decisiones, cada TML debe cumplir criterios estrictos de trazabilidad y calidad de medición, entre los principales aspectos se pueden mencionar los siguientes:\n\n"),                     
                    
            ft.TextSpan("1.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Selección estratégica: son seleccionados considerando el potencial de corrosión generalizada y el riesgo de corrosión localizada del proceso (como zonas de flujo turbulento, codos o puntos bajos).\n\n"),
                    
            ft.TextSpan("2.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Monitoreo y tendencia: se documentan y evalúan periódicamente. La comparación de los espesores medidos en un TML con inspecciones anteriores permite determinar con precisión la velocidad a la cual se desgasta el material.\n\n"),
                    
            ft.TextSpan("3.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Densidad de los TML's: los circuitos de inspección con mayor velocidad de corrosión, fluidos más agresivos o consecuencias graves en caso de fuga, requieren una mayor cantidad de TML's para garantizar una evaluación confiable.\n\n"),
            ]
        )

        

