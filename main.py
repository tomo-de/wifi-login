
import ssl
import macwifi
import requests
import requests
import urllib3
import data


def login() -> None:
    # 現在wifiのssid確認
    now_wifi_ssid = macwifi.get_ssid()
    # 登録リストの取得
    preference = data.preference()
    wifi_list = preference.set_ssid_list

    if now_wifi_ssid not in wifi_list:
        # 切り替えたwifiが登録されているか されていなければ処理を終了
        return
    if check_connected_internet():
        # インターネットに接続されていれば処理を終了
        return
    # ページにリクエストを送る
    request_login(preference.set_user_id, preference.password, preference.url)


def check_connected_internet() -> bool:
    """インターネットに繋がっているか確認する
    """
    try:
        requests.get("https://www.google.com", timeout=3.0)
        return True
    except requests.exceptions.Timeout:
        return False


def request_login(user_id: str, password: str, url: str) -> None:
    """ログインのリクエストを送る
    """
    s = requests.Session()
    s.mount('https://', TLSAdapter())
    payload = {'uid': user_id, 'pwd': password}
    try:
        response = s.post(url, data=payload, timeout=30.0)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print(e)


class TLSAdapter(requests.adapters.HTTPAdapter):
    """requestsにおけるTLSのセキュリティレベルを下げる
    """

    def init_poolmanager(self, connections, maxsize, block=False):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_version=ssl.PROTOCOL_TLS,
            ssl_context=ctx)
