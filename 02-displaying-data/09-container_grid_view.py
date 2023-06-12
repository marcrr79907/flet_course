import os
import flet
from flet import Container, GridView, Page, Text, alignment, border, border_radius, colors

os.environ['FLET_WS_MAX_MESSAGE_SIZE'] = '8000000'


def main(page: Page):
    gvw = GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gvw)

    for i in range(5000):
        gvw.controls.append(
            Container(
                Text(f'Item {i}'),
                alignment=alignment.center,
                bgcolor=colors.AMBER_100,
                border=border.all(1, colors.AMBER_500),
                border_radius=border_radius.all(5),
            )
        )
        # Send page to a page
        if i % 500 == 0:
            page.update()

    # Send the rest to a page
    page.update()


flet.app(target=main, view=flet.WEB_BROWSER)
