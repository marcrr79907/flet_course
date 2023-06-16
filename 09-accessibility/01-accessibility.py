import flet as ft


def main(page: ft.Page):
    page.title = 'Flet App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == 'S' and e.ctrl:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()

    page.on_keyboard_event = on_keyboard

    txt_number = ft.Text('0', size=40)

    def button_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        txt_number,
        ft.Text('Press CTRL+S to toggle semantics debugger'),
        ft.FloatingActionButton(
            icon=ft.icons.ADD, tooltip='Incrementar valor', on_click=button_click)
    )


ft.app(target=main)
