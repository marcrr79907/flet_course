import flet
from flet import Dropdown, ElevatedButton, Page, Text, dropdown


def main(page: Page):

    def show_color(e):
        lbl_text.color = dpn_color.value
        lbl_text.value = f'The color is {dpn_color.value}'
        page.update()

    lbl_text = Text()
    btn_submit = ElevatedButton('Submit', on_click=show_color)
    dpn_color = Dropdown(
        width=100,
        options=[
            dropdown.Option('Red'),
            dropdown.Option('Blue'),
            dropdown.Option('Green')
        ]
    )

    page.add(dpn_color, btn_submit, lbl_text)


flet.app(target=main)
