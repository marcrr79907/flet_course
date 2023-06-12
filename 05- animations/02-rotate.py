from math import pi
import flet as ft


def main(page: ft.Page):

    container = ft.Container(
        width=100,
        height=70,
        bgcolor='blue',
        border_radius=5,
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(
            500, ft.AnimationCurve.BOUNCE_OUT)
    )

    def animate(e):
        container.rotate.angle += pi / 2
        container.bgcolor = 'green'
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(
        container,
        ft.ElevatedButton('Animate', on_click=animate)
    )


ft.app(target=main)
