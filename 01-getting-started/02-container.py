import flet
from flet import Page, Row, Text


def main(page: Page):
    elements = [Text('Icon'), Text('Text'), Text('Image')]
    row_date = Row(controls=elements)

    page.add(row_date)


flet.app(target=main)
