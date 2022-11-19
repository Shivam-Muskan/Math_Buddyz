from typing import List

import flet as ft
from flet import Control


def home(page) -> List[Control]:
    return [
        ft.AppBar(title=ft.Text("Home"), bgcolor=ft.colors.SURFACE_VARIANT),
        ft.ElevatedButton("Go to matrix solver", on_click=lambda _: page.go("/matrix")),
    ]
