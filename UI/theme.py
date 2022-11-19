from flet import Page, theme, colors


def page_theme(page: Page):
    DARK_SEED_COLOR = colors.INDIGO

    page.title = "Math Buddyz"
    page.theme_mode = "dark"
    page.dark_theme = theme.Theme(color_scheme_seed=DARK_SEED_COLOR, use_material3=True)
    page.update()
