import flet
from flet import ElevatedButton, Page, Text, TextField


def main(page: Page):

    def event_click(e):
        if not txt_name.value:
            txt_name.error_text = 'Por favor ingrese su nombre'
            page.update()

        else:
            name = txt_name.value
            page.clean()
            page.add(Text(f'Hello...{name}'))

    txt_name = TextField(label='Nombre')

    page.add(txt_name, ElevatedButton('Acept', on_click=event_click))


flet.app(target=main)
