import flet as ft
from flet import View

from UI.routes import home, matrix


def route_view(page):
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                home(page)
            )
        )
        if page.route == "/matrix":
            page.views.append(
                View(
                    "/matrix",
                    matrix(page)
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
