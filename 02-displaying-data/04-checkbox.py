import flet
from flet import Checkbox, Page, Text


def main(page: Page):

    def task_checked(e):
        if chk_task.value:
            lbl_status.color = 'green'
            lbl_status.value = f'{chk_task.label} successfuly!'
        else:
            lbl_status.color = 'red'
            lbl_status.value = f'{chk_task.label} in course!'

        page.update()

    chk_task = Checkbox(label='Learn Python', value=False,
                        on_change=task_checked)
    lbl_status = Text()

    page.add(chk_task, lbl_status)


flet.app(target=main)
