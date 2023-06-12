import flet as ft


def main(page: ft.Page):

    container = ft.Container(
        width=150,
        height=150,
        bgcolor='blue',
        border_radius=10,
        offset=ft.transform.Offset(-2, 0),
        animate_offset=ft.animation.Animation(2000)
    )

    def animate(e):
        if container.offset.x == 4:
            container.offset = ft.transform.Offset(-2, 0)
        else:
            container.offset = ft.transform.Offset(4, 0)

        container.update()

    page.add(
        container,
        ft.ElevatedButton('Animate', on_click=animate)
    )


ft.app(target=main)
