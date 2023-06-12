import flet
from flet import Column, ElevatedButton, Page, Row, TextField, Text


def main(page: Page):
    txt_first_name = TextField(autofocus=True)
    txt_last_name = TextField()

    lbl_first_name = Text()
    lbl_last_name = Text()
    col_date = Column([lbl_first_name, lbl_last_name], width=300)
    col_date.disabled = True

    def send_date(event):
        lbl_first_name.value = txt_first_name.value
        lbl_last_name.value = txt_last_name.value
        col_date.disabled = False

        txt_first_name.value = ''
        txt_last_name.value = ''

        page.update()
        txt_first_name.focus()

    btn_send = ElevatedButton(text='Send', on_click=send_date)

    col = Column([txt_first_name, txt_last_name, btn_send], width=300)

    row = Row([col, col_date], alignment='center')

    page.add(row)


flet.app(target=main, view=flet.WEB_BROWSER)
