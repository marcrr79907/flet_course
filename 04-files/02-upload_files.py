from typing import Dict

import flet
from flet import (
    Column,
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Page,
    ProgressRing,
    Ref,
    Row,
    Text,
    icons
)


def main(page: Page):
    pbr: Dict[str, ProgressRing] = {}
    files = Ref[Column]()
    upload_button = Ref[ElevatedButton]()

    def file_picker_result(e: FilePickerResultEvent):
        upload_button.current.disabled = True if e.files == None else False
        pbr.clear()
        files.current.controls.clear()

        if e.files != None:
            for f in e.files:
                pbr_files = ProgressRing(
                    value=0, bgcolor='#eeeeee', width=20, height=20)
                pbr[f.name] = pbr_files
                files.current.controls.append(Row([pbr_files, Text(f.name)]))
        page.update()

    def on_upload_progress(e: FilePickerUploadEvent):
        pbr[e.file_name].value = e.progress
        pbr[e.file_name].update()

    file_picker = FilePicker(on_result=file_picker_result,
                             on_upload=on_upload_progress)

    def upload_files(e):
        uf_list = []
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                uf_list.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600)
                    )
                )
            file_picker.upload(uf_list)
    # hide dialog in a overlay
    page.overlay.append(file_picker)

    page.add(
        ElevatedButton(
            'Select files...',
            icon=icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(allow_multiple=True)
        ),
        Column(ref=files),
        ElevatedButton(
            'Upload',
            ref=upload_button,
            icon=icons.UPLOAD,
            on_click=upload_files,
            disabled=True
        )
    )


flet.app(target=main, upload_dir='uploads', view=flet.WEB_BROWSER)
