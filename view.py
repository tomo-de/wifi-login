import rumps
import flet as ft
import data
import main

def config_page(page: ft.Page):
    # add/update controls on Page
    page.title = "設定"
    page.window_width = 600
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    d = data.preference()
    uid = ft.TextField(
        value=d.user_id, text_align=ft.TextAlign.RIGHT, width=300)
    pwd = ft.TextField(
        value=d.password, text_align=ft.TextAlign.RIGHT, width=300, password=True, can_reveal_password=True)
    url = ft.TextField(
        value=d.url, text_align=ft.TextAlign.RIGHT, width=300, hint_text="https://example.com/")
    ssid_list = ft.TextField(
        value=",".join(d.ssid_list), text_align=ft.TextAlign.RIGHT, width=300, hint_text="xxx,yyy,zzz")
    
    def handle_click_apply_button(e):
        d = data.preference()
        d.set_user_id(uid.value)
        d.set_password(pwd.value)
        d.set_url(url.value)
        d.set_ssid_list(ssid_list.value)
        page.update()

    page.add(
        ft.Column(
            [
                # uid
                ft.Row(
                    [
                        ft.Container(content=ft.Text(
                            value="ログインID"), width=100),
                        uid
                    ]
                ),
                # pwd
                ft.Row(
                    [
                        ft.Container(content=ft.Text(
                            value="パスワード"), width=100),
                        pwd
                    ]
                ),
                ft.Row(
                    [
                        ft.Container(content=ft.Text(value="url"), width=100),
                        url
                    ]
                ),
                ft.Row(
                    [
                        ft.Container(content=ft.Text(
                            value="ssidのリスト"), width=100),
                        ssid_list
                    ]
                ),
                ft.Container(
                    alignment=ft.alignment.center_right,
                    content=ft.FilledButton(text="適用", on_click=handle_click_apply_button)
                )
                
            ]
        )
    )

class App(rumps.App):
    @rumps.clicked("設定")
    def config(self, _):
        ft.app(target=config_page)

    @rumps.clicked("ログイン")
    def login(self, _):
        main.login()
    
    @rumps.timer(15)
    def check_login(self, _):
        main.login()

if __name__ == "__main__":
    app = App("wifi-login").run()
    app.run()