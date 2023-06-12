import flet
from flet import Page, Text


def main(page: Page):

    lbl_text = Text(
        value='Flet for frontend',
        size=30,
        color='red',
        bgcolor='black',
        weight='bold',
        italic=True
    )

    page.add(lbl_text)


flet.app(target=main, view=flet.WEB_BROWSER)
