import time
from threading import Thread

import flet as ft


class Countdown(ft.UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.thread = Thread(target=self.update_timer, args=(), daemon=True)
        self.thread.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = f'{mins: 02d}:{secs: 02d}'
            self.update()
            time.sleep(1)
            self.seconds -= 1
        self.update()

    def build(self):
        self.countdown = ft.Text()
        return self.countdown


def main(page: ft.Page):
    page.add(Countdown(100), Countdown(130))


if __name__ == "__main__":
    ft.app(target=main)
