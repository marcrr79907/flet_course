import flet
from flet import Page, ElevatedButton, Text, TextField, Row


def main(page: Page):

    txt_name = TextField(label='Nombre')
    label_saludo = Text()

    def saludo(event):
        label_saludo.value = f'Hola...{txt_name.value}'
        page.update()

    elements = [txt_name,
                ElevatedButton(text='Saludar', on_click=saludo),
                label_saludo]
    row = Row(controls=elements)

    page.add(row)


flet.app(target=main)
