# vistas/vistas_tml.py
import flet as ft
from config import COLOR_TEXTO_TITULO, COLOR_TEXTO_CUERPO

def crear_vista_consideracion(titulo: str,
                         parrafos: list,
                         icono: ft.IconData= ft.Icons.INFO_OUTLINE_ROUNDED):
    #Parrafo 1
    p1 = ft.Text(
        value=parrafos[0],
        size=20,
        color=COLOR_TEXTO_CUERPO,
        text_align=ft.TextAlign.JUSTIFY,
    )
    #Parrafo 2
    p2 = ft.Container(
        content=ft.Text(
            value=parrafos[1],
            size=25,
            color=COLOR_TEXTO_CUERPO,
            text_align=ft.TextAlign.JUSTIFY,
        ),
        border=ft.Border(left=ft.BorderSide(width=4, color=ft.Colors.BLUE_600)),
        padding=ft.Padding.only(left=15, top=10, bottom=10, right=10),
        bgcolor=ft.Colors.BLUE_50,
        border_radius=ft.BorderRadius.only(top_right=8, bottom_right=8),
    )
    #Parrafo 3
    p3 = ft.Text(
        value=parrafos[2],
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
                content= ft.Column(
                    controls=[p1, p2, p3],
                    spacing=15,
                ),
                padding=ft.Padding.only(left=40, right=40)
            )
        ],
        spacing=20,
    )



class ConsideracionPracticaView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = crear_vista_consideracion(
            "Consideraciones prácticas",

            [
                (
                    "Cuando se va a inspeccionar un activo, debemos asignar un TML. Podemos establecer fácilmente la ubicación espacial del punto en cuestión, pero en cuanto a dimensión se refiere muchas veces deja de ser punto y se convierte en un circulo."
                ),

                (
                    "Por ejemplo: se utiliza un marcador punta gruesa y de manera casi instintiva no se apoya y se retira dejando una marca suave (punto), comunmente lo que se hace es apoyar y hacer un movimiento circular con el marcador sobre la superficie del activo a inspeccionar, quedando definida una pequeña área o círculo. Para efectos prácticos está área definida por un circulo y cuyo diámetro será menor o igual al diámetro del transductor/palpador/sonda se seguirá considerando o llamado \"punto\"."
                ),

                (
                    "Más allá de la teoría dictada por los códigos de inspección, la ejecución efectiva de un plan de inspección/monitoreo depende de las condiciones bajo las cuales el inspector debe operar, el críterio y las buenas prácticas."
                )
            ]
            
        )