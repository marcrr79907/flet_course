import flet as ft


class Counter(ft.UserControl):
    def __init__(self, initial_value=0):
        super().__init__()
        self.counter = initial_value

    def add_click(self, e):
        self.counter += 1
        self.lbl_count.value = str(self.counter)
        self.update()

    def build(self):
        self.lbl_count = ft.Text(str(self.counter))

        return ft.Row([
            self.lbl_count,
            ft.ElevatedButton('Add', on_click=self.add_click)
        ])


def main(page: ft.Page):
    page.add(Counter(), Counter(100))


if __name__ == "__main__":
    ft.app(target=main)
