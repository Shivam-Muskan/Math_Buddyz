from typing import List

import flet as ft
from flet import Control


def matrix(page) -> List[Control]:
    return [
        ft.AppBar(title=ft.Text("Matrix"), bgcolor=ft.colors.SURFACE_VARIANT),
        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
    ]
