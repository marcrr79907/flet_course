import flet
from flet import Checkbox, ElevatedButton, Page, Row, TextField


def main(page: Page):

    def add_task(event):
        page.add(Checkbox(label=txt_task.value))
        txt_task.value = ''
        page.update()

    txt_task = TextField(hint_text='Add task', width=200)
    btn_add_task = ElevatedButton(text='add', on_click=add_task)

    page.add(Row([txt_task, btn_add_task]))


flet.app(target=main)
