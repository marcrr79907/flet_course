import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


def main(page: Page):
    page.title = 'Navigation Routing'
    print('Ruta inicial', page.route)

    def route_change(e):
        print('Ruta cambiada', e.route)
        page.views.clear()

        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Flet app')),
                    ElevatedButton('Go to configuratios',
                                   on_click=open_settings)
                ]
            )
        )
        if page.route == '/settings' or page.route == '/settings/mail':
            page.views.append(
                View(
                    '/settings',
                    [
                        AppBar(title=Text(
                            'Settings', bgcolor=colors.SURFACE_VARIANT)),
                        Text('Configurations', style='bodyMedium'),
                        ElevatedButton('Go to mail settings',
                                       on_click=open_mail_settings)
                    ]
                )
            )
        if page.route == '/settings/mail':
            page.views.append(
                View(
                    '/settings/mail',
                    [
                        AppBar(title=Text('Mail'),
                               bgcolor=colors.SURFACE_VARIANT),
                        Text('Mail settings')
                    ]
                )
            )

        page.update()

    def view_pop(e):
        print('View pop: ', e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_settings(e):
        page.go('/settings')

    def open_mail_settings(e):
        page.go('/settings/mail')

    page.go(page.route)


flet.app(target=main, view=flet.WEB_BROWSER)
