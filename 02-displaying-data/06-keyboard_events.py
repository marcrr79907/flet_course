import flet
from flet import KeyboardEvent, Page, Text


def main(page: Page):

    def on_keyboard(e: KeyboardEvent):
        page.add(
            Text(
                f'Key: {e.key} Shift: {e.shift} Control: {e.ctrl} Alt: {e.alt} Meta: {e.meta}'
            )
        )

    page.on_keyboard_event = on_keyboard
    page.add(Text('Press any key'))


flet.app(target=main)
