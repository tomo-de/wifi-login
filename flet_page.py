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
    ssid_list = ft.TextField(
        value=",".join(d.ssid_list), width=text_field_width, hint_text="Xtou_1F,Toshokan_1F,Ytou_1F_A")

    def handle_click_apply_button(e):
        d = data.preference()
        d.set_user_id(uid.value)
        d.set_password(pwd.value)
        d.set_url(url.value)
        d.set_ssid_list(ssid_list.value)
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
                    ft.Row(
                        [
                            ft.Container(content=ft.Text(
                                value="wifiの表示名"), width=text_width),
                            ssid_list
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
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
