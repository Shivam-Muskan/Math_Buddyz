import flet
from flet import ElevatedButton, Page, Text, colors, icons, theme
from flet.app_bar import AppBar
from flet.icon import Icon
from flet.icon_button import IconButton
from flet.popup_menu_button import PopupMenuButton, PopupMenuItem
from flet.row import Row
from UI import page_theme, route_view


def main(page: Page):
    page_theme(page)
    route_view(page)
    page.update()

    page.padding = 50
    page.add(Text("Body!"), ElevatedButton("Click me!"))


flet.app(target=main)
