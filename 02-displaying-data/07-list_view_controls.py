import flet
from flet import ListView, Page, Text


def main(page: Page):

    lvw_texts = ListView(expand=True, spacing=10)

    for i in range(5000):
        lvw_texts.controls.append(Text(f'Line {i}'))

    page.add(lvw_texts)


flet.app(target=main, view=flet.WEB_BROWSER)
