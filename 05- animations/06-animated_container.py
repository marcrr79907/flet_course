import flet
from flet import Container, ElevatedButton, Page


def main(page: Page):

    c = Container(
        width=150,
        height=150,
        bgcolor='red',
        animate=flet.animation.Animation(1000, flet.AnimationCurve.DECELERATE)
    )

    def animated_container(e):
        c.width = 100 if c.width == 150 else 150
        c.height = 50 if c.height == 150 else 150
        c.bgcolor = 'blue' if c.bgcolor == 'red' else 'red'
        c.update()

    page.add(c, ElevatedButton('Animate', on_click=animated_container))


flet.app(target=main)
