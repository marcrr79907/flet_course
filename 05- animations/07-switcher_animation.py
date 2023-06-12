import time
import flet
from flet import ElevatedButton, Image, Page


def main(page: Page):

    image = Image(src='https://picsum.photos/150/150', width=150, height=150)

    def animate(e):
        sw.content = Image(
            src=f'https://picsum.photos/150/150?{time.time()}',
            width=150, height=150
        )
        page.update()

    sw = flet.AnimatedSwitcher(
        image,
        transition=flet.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=500,
        switch_in_curve=flet.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=flet.AnimationCurve.BOUNCE_IN
    )

    page.add(
        sw,
        ElevatedButton('Animate', on_click=animate)
    )


flet.app(target=main)
