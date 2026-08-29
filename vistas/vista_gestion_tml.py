from typing import Union, List
import flet as ft
from config import COLOR_TEXTO_TITULO, COLOR_TEXTO_CUERPO


def crear_tabla_tml_cml():
    """Crea la tabla comparativa entre TML y CML con encabezados perfectamente centrados."""

    filas_datos = [
        (
            "Punto específico designado exclusivamente para monitorear espesor de pared de un activo.",
            "Zona o área designada para un tipo de mecanismo de daño."
        ),
        (
            "Utiliza específicamente Ultrasonido (UT) o radiografía para recolectar datos cuantitativos de pérdida de material (espesor).",
            "Puede incluir ultrasonido, técnicas cualitativas (partículas magnetizables, inspección visual, etc.)."
        ),
        (
            "Se enfoca en corrosión generalizada/localizada o erosión.",
            "Abarca agrietamiento, daño térmico, alteración metalúrgica y pérdida de espesor."
        ),
        (
            "Un TML es técnicamente un tipo de CML especializado.",
            "Todos los TML son CML, pero no todos los CML son TML."
        )
    ]

    color_borde = ft.Colors.BLACK

    return ft.DataTable(
        heading_row_color=ft.Colors.GREY_300,
        heading_row_height=45,
        data_row_min_height=60,
        data_row_max_height=float("inf"),
        column_spacing=0,
        expand=True,  # Hace que la tabla ocupe todo el ancho disponible
        border=ft.Border.all(1.5, color_borde),
        vertical_lines=ft.BorderSide(1, color_borde),
        horizontal_lines=ft.BorderSide(1, color_borde),
        columns=[
            ft.DataColumn(
                label=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "                                                        TML",
                                weight=ft.FontWeight.BOLD,
                                color=COLOR_TEXTO_TITULO,
                                size=16,
                                text_align=ft.TextAlign.CENTER,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    alignment=ft.Alignment(0, 0),  # Centrado absoluto en X e Y
                    expand=True,
                )
            ),
            ft.DataColumn(
                label=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "                                                   CML",
                                weight=ft.FontWeight.BOLD,
                                color=COLOR_TEXTO_TITULO,
                                size=16,
                                text_align=ft.TextAlign.CENTER,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    alignment=ft.Alignment(0, 0),  # Centrado absoluto en X e Y
                    expand=True,
                )
            ),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Container(
                            content=ft.Text(
                                tml_texto,
                                text_align=ft.TextAlign.JUSTIFY,
                                color=COLOR_TEXTO_CUERPO,
                                size=14,
                            ),
                            padding=10,
                            alignment=ft.Alignment(-1, -1),
                            expand=True,
                        )
                    ),
                    ft.DataCell(
                        ft.Container(
                            content=ft.Text(
                                cml_texto,
                                text_align=ft.TextAlign.JUSTIFY,
                                color=COLOR_TEXTO_CUERPO,
                                size=14,
                            ),
                            padding=10,
                            alignment=ft.Alignment(-1, -1),
                            expand=True,
                        )
                    ),
                ]
            )
            for tml_texto, cml_texto in filas_datos
        ],
    )


def crear_vista_gestion(
    titulo: str,
    descripcion: Union[str, List[ft.TextSpan]],
    icono: ft.IconData = ft.Icons.MENU_BOOK_OUTLINED,
):
    if isinstance(descripcion, list):
        texto_control = ft.Text(
            spans=descripcion,
            size=20,
            color=COLOR_TEXTO_CUERPO,
            text_align=ft.TextAlign.JUSTIFY,
        )
    else:
        texto_control = ft.Text(
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
                        border_radius=ft.BorderRadius.only(
                            top_right=8, bottom_right=8
                        ),
                        border=ft.Border.only(
                            left=ft.BorderSide(width=4, color=ft.Colors.BLUE_600)
                        ),
                    ),
                    ft.Text(
                        value=titulo,
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color=COLOR_TEXTO_TITULO,
                        width=float("inf"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
            ),
            ft.Container(
                content=texto_control,
                padding=ft.Padding.only(left=40, right=40),
            ),
            ft.Container(
                content=crear_tabla_tml_cml(),
                padding=ft.Padding.only(left=40, right=40, top=10, bottom=20),
            )
        ],
        spacing=20,
    )


class GestionDatosView(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = crear_vista_gestion(
            "Gestión de datos (CML vs. TML)",
            [
                ft.TextSpan("En el ámbito de integridad mecánica, los TML's se agrupan o forman parte de los CML's. Aunque en ocasiones se usan como sinónimos, técnicamente:\n\n"),
                ft.TextSpan("CML: ", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan("es el área general o zona que se monitorea.\n"),
                ft.TextSpan("TML: ", ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.TextSpan("es el área específica o punto específico dentro de esa área (CML) donde se realiza una medición para monitorear el espesor de pared de un activo (tuberías, recipientes a presión, etc.)."),
            ]
        )