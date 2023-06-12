import flet as ft


def main(page: ft.Page):

    container = ft.Container(
        width=150,
        height=150,
        bgcolor='blue',
        border_radius=10,
        animate_opacity=1000
    )

    def animate_opacity(e):
        container.opacity = 0 if container.opacity == 1 else 1
        container.update()

    page.add(
        container,
        ft.ElevatedButton(
            'Animate Opacity',
            on_click=animate_opacity
        )
    )


ft.app(target=main)
