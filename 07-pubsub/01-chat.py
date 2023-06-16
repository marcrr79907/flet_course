import flet as ft
from flet import Column, ElevatedButton, Page, Row, Text, TextField, icons


def main(page: Page):
    page.title = 'ChatApp'

    def on_message(msg):
        messages.controls.append(Text(msg))
        page.update()

    page.pubsub.subscribe(on_message)

    def send_click(e):
        page.pubsub.send_all(f'{user.value}: {message.value}')

        message.value = ''
        page.update()

    messages = Column()
    user = TextField(hint_text='Your name', width=150)
    message = TextField(hint_text='Your message...', expand=True)
    send = ElevatedButton(
        'Send', icon=icons.SEND, on_click=send_click)

    page.add(
        messages,
        Row(
            [user, message, send]
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)
