from typing import Callable, Self
import flet as ft
import data


def config_page(page: ft.Page):
    # add/update controls on Page
    page.title = "設定"
    page.window_width = 707
    page.window_height = 500
    # page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_width = 100
    text_field_width = 400
    d = data.preference()
    uid = ft.TextField(
        value=d.user_id, width=text_field_width)
    pwd = ft.TextField(
        value=d.password, width=text_field_width, password=True, can_reveal_password=True)
    url = ft.TextField(
        value=d.url, width=text_field_width, hint_text="https://example.com/")
    ssid_list = SsidList(text_width, text_field_width, d.ssid_list)

    def handle_click_apply_button(e):
        d = data.preference()
        d.set_user_id(uid.value)
        d.set_password(pwd.value)
        d.set_url(url.value)
        d.set_ssid_list(",".join(map(str, ssid_list.get_list())))
        # スナックバー
        page.snack_bar = ft.SnackBar(
            ft.Row([ft.Icon(name=ft.icons.CHECK_CIRCLE, color="#4eac55", size=20), ft.Text("設定が保存されました")]), bgcolor="#b6ebcd")
        page.snack_bar.open = True
        page.update()

    page.add(
        ft.Container(
            padding=10,
            content=ft.Column(
                [
                    # uid
                    ft.Row(
                        [
                            ft.Container(content=ft.Text(
                                value="ログインID"), width=text_width),
                            uid,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    # pwd
                    ft.Row(
                        [
                            ft.Container(content=ft.Text(
                                value="パスワード"), width=text_width),
                            pwd
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Container(content=ft.Text(
                                value="url"), width=text_width),
                            url
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ssid_list,
                    ft.Row(
                        [
                            ft.Container(
                                width=text_width+text_field_width,
                                alignment=ft.alignment.center_right,
                                content=ft.ElevatedButton(
                                    content=ft.Container(
                                        content=ft.Text(value="保存", size=15),
                                        padding=ft.padding.symmetric(7, 12)
                                    ),
                                    on_click=handle_click_apply_button)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ]
            )
        )
    )


class SsidListItem(ft.UserControl):
    """ssidのリストビュー内のアイテム
    """

    def __init__(self, text: str | None, delete_func: Callable[[Self], None]):
        super().__init__()
        self.text = text
        self.delete_func = delete_func

    def build(self):
        self.display_text = ft.Text(value=self.text)

        return ft.Container(ft.Row(
            [self.display_text, ft.IconButton(
                icon=ft.icons.DELETE,
                icon_size=20,
                tooltip="削除",
                on_click=self.delete_clicked,
            ),], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor=ft.colors.PRIMARY_CONTAINER, height=50, border_radius=10, padding=10)

    def delete_clicked(self, e):
        """コンストラクタで渡された削除関数を実行する関数
        """
        self.delete_func(self)

    def get_text(self) -> str | None:
        """リストビューのアイテムがもつssid名を返す関数

        Returns:
            str | None: ssid名
        """
        return self.text


class SsidList(ft.UserControl):
    """ssidのテキストフィールドおよびssidのリストビュー
    """

    def __init__(self, text_width, text_field_width, ssid_list: list[str]):
        super().__init__()
        self.text_field_width = text_field_width
        self.text_width = text_width
        # ssid名のリストを受け取る
        self.ssid_list = ssid_list

    def build(self):
        self.enter_text = ft.TextField(
            width=self.text_field_width, hint_text="Xtou_1F", on_submit=self.handle_fill_ssid_textfield)
        self.ssid_list_view = ft.ListView(
            width=self.text_width+self.text_field_width, height=150, spacing=10, padding=0, auto_scroll=True)
        for i in self.ssid_list:
            text = SsidListItem(i, self.delete_ssid_list_item)
            self.ssid_list_view.controls.append(text)

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(content=ft.Text(
                            value="wifiの表示名"), width=self.text_width),
                        self.enter_text,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([self.ssid_list_view],
                       alignment=ft.MainAxisAlignment.CENTER),
            ],
        )

    def handle_fill_ssid_textfield(self, e):
        """ssidのテキストフィールドが記入されエンターを押されたとき,ssidリストビューとssidリストを書き換える
        """
        text = SsidListItem(self.enter_text.value, self.delete_ssid_list_item)
        self.ssid_list.append(self.enter_text.value)
        self.ssid_list_view.controls.append(text)
        self.enter_text.value = ""
        self.update()

    def delete_ssid_list_item(self, ssid_list_item: SsidListItem):
        """ssidリストビューおよびssidリストのアイテムを削除する関数
        """
        self.ssid_list.remove(ssid_list_item.get_text())
        self.ssid_list_view.controls.remove(ssid_list_item)
        self.update()

    def get_list(self) -> list[str]:
        """ssidリストを取得する関数

        Returns:
            list[str]: リストビューと同じデータをもつstrのリスト
        """
        return self.ssid_list
