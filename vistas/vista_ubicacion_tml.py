from typing import Union, List
import flet as ft
from config import COLOR_TEXTO_TITULO, COLOR_TEXTO_CUERPO

def crear_vista_ubicacion(
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



class UbicacionView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = crear_vista_ubicacion(
            "Ubicación de los TML's",

            [
            ft.TextSpan("La ubicación de los TML´s no es aleatoria. Su distribución debe centrarse en áreas donde las condiciones físiccas o químicas promuevan la pérdida de material. El área de integridad y corrosión utiliza P&ID´s y la experiencia operativa para identificar los componentes más vulnerables. Entre las zonas más destacadas de un circuito de inspección los puntos más críticos se pueden ubicar en:\n\n"),                     
                                
            ft.TextSpan("1.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Puntos bajos.\n"),
                                
            ft.TextSpan("2.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Cambios de dirección (Codos).\n"),
                                
            ft.TextSpan("3.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Uniones soldadas.\n"),
            
            ft.TextSpan("4.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Reducciones.\n"),
            
            ft.TextSpan("5.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Líneas con flujo turbulento.\n"),
            
            ft.TextSpan("6.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Zonas de choque (tee).\n"),
            
            ft.TextSpan("7.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Deadlegs (tramos muertos, zonas muertas, piernas muertas).\n"),
            
            ft.TextSpan("8.", ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(" Puntos de inyección y mezcla.\n\n"),
            
            ft.TextSpan("Los puntos más críticos del circuito de inspección se establecen considerando factores como el riesgo de corrosión específica del servicio, velocidad de flujo del fluido y zonas de inyección."),
            ]
        )

            

