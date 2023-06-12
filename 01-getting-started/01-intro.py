import time

import flet
from flet import Page, Text


def main(page: Page):
    label_txt = Text()
    page.add(label_txt)

    for i in range(10):
        label_txt.value = f'Second(s): {i}'
        page.update()

        time.sleep(1)


flet.app(target=main)
