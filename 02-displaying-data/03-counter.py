import flet
from flet import IconButton, Page, Row, TextField, icons


def main(page: Page):

    page.title = 'Counter'
    page.vertical_alignment = 'center'
    txt_number = TextField(value='0', width=100, text_align='center')

    def minus_click(event):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(event):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    btn_remove = IconButton(icons.REMOVE, on_click=minus_click)
    btn_plus = IconButton(icons.ADD, on_click=plus_click)

    row = Row(controls=[btn_remove, txt_number, btn_plus],
              alignment='center')

    page.add(row)


flet.app(target=main)
