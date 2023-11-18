import rumps
import flet as ft


def main(page: ft.Page):
    # add/update controls on Page
    pass


class App(rumps.App):
    @rumps.clicked("Config")
    def hello_world(self, _):
        ft.app(target=main)

    def login(self, sender):
        pass

if __name__ == "__main__":
    app = App("wifi-login").run()
    app_timer = rumps.Timer(app.login(), 60)
    app.start()
    app.run()