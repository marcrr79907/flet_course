import flet as ft


def main(page: ft.Page):

    container = ft.Container(
        width=100,
        height=100,
        bgcolor='blue',
        border_radius=5,
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(
            600, ft.AnimationCurve.BOUNCE_IN_OUT)
    )

    def animate(e):
        if container.scale == 2:
            container.scale = 1
        else:
            container.scale = 2

        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(
        container,
        ft.ElevatedButton('Animate', on_click=animate)
    )


ft.app(target=main)
