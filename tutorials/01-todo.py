import flet as ft


class Task(ft.UserControl):
    def __init__(self, task_name, delete_task):
        super().__init__()
        self.task_name = task_name
        self.delete_task = delete_task

    def build(self):

        self.chb_display_task = ft.Checkbox(value=False, label=self.task_name)
        self.txt_edit_name = ft.TextField(expand=1, autofocus=True)

        self.row_display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.chb_display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip='Edit To-Do',
                            on_click=self.edit_task
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            tooltip='Delete To-Do',
                            on_click=self.delete_clicked
                        )
                    ]
                )
            ]
        )

        self.row_edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.txt_edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip='Update To-Do',
                    on_click=self.save_task
                )
            ]
        )

        return ft.Column(controls=[self.row_display_view, self.row_edit_view])

    def edit_task(self, e):
        self.txt_edit_name.value = self.chb_display_task.label
        self.row_display_view.visible = False
        self.row_edit_view.visible = True
        self.update()

    def save_task(self, e):
        self.chb_display_task.label = self.txt_edit_name.value
        self.row_display_view.visible = True
        self.row_edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.delete_task(self)


class TodoApp(ft.UserControl):

    def build(self):
        self.txt_new_task = ft.TextField(
            hint_text='Que tarea deseas agregar?', expand=True, autofocus=True)
        self.btn_add_task = ft.FloatingActionButton(
            icon=ft.icons.ADD, on_click=self.add_task_clicked)

        self.col_tasks = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.txt_new_task,
                        self.btn_add_task
                    ]
                ),
                self.col_tasks
            ]
        )

    def add_task_clicked(self, e):
        task = Task(self.txt_new_task.value, self.delete_task)
        self.col_tasks.controls.append(task)
        self.txt_new_task.focus()
        self.txt_new_task.value = ''
        self.update()

    def delete_task(self, task):
        self.col_tasks.controls.remove(task)
        self.update()


def main(page: ft.Page):

    page.title = 'To Do App'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    page.add(todo)


ft.app(target=main)
