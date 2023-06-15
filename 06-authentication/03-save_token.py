import json
import os

import flet as ft
import httpx
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
from flet.security import decrypt, encrypt

MY_APP_SECRET_KEY = os.getenv("MY_APP_SECRET_KEY")
assert MY_APP_SECRET_KEY, "set MY_APP_SECRET_KEY environment variable"
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
assert GITHUB_CLIENT_ID, "set GITHUB_CLIENT_ID environment variable"
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
assert GITHUB_CLIENT_SECRET, "set GITHUB_CLIENT_SECRET environment variable"


def main(page: ft.Page):
    # encryption passphrase
    secret_key = MY_APP_SECRET_KEY

    # configure provider
    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    # client storage keys
    AUTH_TOKEN_KEY = "myapp.auth_token"

    def perform_login(e):
        # perform login
        saved_token = None
        ejt = page.client_storage.get(AUTH_TOKEN_KEY)
        if ejt:
            saved_token = decrypt(ejt, secret_key)
        if e is not None or saved_token is not None:
            page.login(provider, saved_token=saved_token,
                       scope=["public_repo"])

    def on_login(e: ft.LoginEvent):
        if e.error:
            raise Exception(e.error)

        # save token in a client storage
        jt = page.auth.token.to_json()
        ejt = encrypt(jt, secret_key)
        page.client_storage.set(AUTH_TOKEN_KEY, ejt)

        logged_user.value = f"Hello, {page.auth.user['login']}!"
        toggle_login_buttons()
        list_github_repositories()
        page.update()

    def list_github_repositories():
        repos_view.controls.clear()
        if page.auth:
            headers = {
                "User-Agent": "Flet",
                "Authorization": "Bearer {}".format(page.auth.token.access_token),
            }
            repos_resp = httpx.get(
                "https://api.github.com/user/repos", headers=headers)
            repos_resp.raise_for_status()
            user_repos = json.loads(repos_resp.text)
            for repo in user_repos:
                repos_view.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.FOLDER_ROUNDED),
                        title=ft.Text(repo["full_name"]),
                    )
                )

    def logout_button_click(e):
        page.client_storage.remove(AUTH_TOKEN_KEY)
        page.logout()

    def on_logout(e):
        toggle_login_buttons()
        list_github_repositories()
        page.update()

    def toggle_login_buttons():
        login_button.visible = page.auth is None
        logged_user.visible = logout_button.visible = page.auth is not None

    logged_user = ft.Text()
    login_button = ft.ElevatedButton(
        "Login with GitHub", on_click=perform_login)
    logout_button = ft.ElevatedButton("Logout", on_click=logout_button_click)
    repos_view = ft.ListView(expand=True)
    page.on_login = on_login
    page.on_logout = on_logout
    toggle_login_buttons()
    perform_login(None)
    page.add(ft.Row([logged_user, login_button, logout_button]), repos_view)


ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
