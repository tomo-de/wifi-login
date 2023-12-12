import os
import sys
import rumps
import flet as ft
import main
import flet_page


class App(rumps.App):
    @rumps.clicked("設定")
    def config(self, _):
        ft.app(target=flet_page.config_page)
        # アプリの再起動
        os.execl(sys.executable, sys.executable, * sys.argv)

    @rumps.clicked("ログイン")
    def login(self, _):
        main.login()

    @rumps.timer(15)
    def check_login(self, _):
        main.login()


if __name__ == "__main__":
    app = App("wifi-login", icon="assets/key.png", quit_button="終了").run()
    app.run()
