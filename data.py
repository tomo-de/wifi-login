import keyring

class preference:
    """設定情報の管理
    """

    def __init__(self) -> None:
       self.update()
    
    def set_user_id(self, user_id: str) -> None:
        """user idを設定する

        Args:
            user_id (str): 設定するuser id
        """
        keyring.set_password("wifi-login", "user_id", user_id)
        self.update()
    
    def set_password(self, password: str) -> None:
        """passwordを設定する

        Args:
            password (str): 設定するpassword
        """
        keyring.set_password("wifi-login", "password", password)
        self.update()
    
    def set_url(self, url: str) -> None:
        """urlを設定する

        Args:
            url (str): 設定するurl
        """
        keyring.set_password("wifi-login", "url", url)
        self.update()
    
    def set_ssid_list(self, ssid_list: str) -> None:
        """ssid_listを設定する

        Args:
            ssid_list (str): 設定するssid_list
        """
        keyring.set_password("wifi-login", "ssid_list", ssid_list)
        self.update()
    
    def update(self) -> None:
        """keyringに保存された各値を読み込む関数
        """
        # user_id
        user_id = keyring.get_password("wifi-login", "user_id")
        self.user_id = self.__change_str(user_id)

        # password
        password = keyring.get_password("wifi-login", "password")
        self.password = self.__change_str(password)

        # url
        url = keyring.get_password("wifi-login", "url")
        self.url = self.__change_str(url)

        # ssid_list
        ssid_list_str = keyring.get_password("wifi-login", "ssid_list")
        if type(ssid_list_str) is str:
            self.ssid_list = ssid_list_str.split(',')
        else:
            self.ssid_list = []
    
    def __change_str(self, s :str | None):
        """値がstrであればstrを返し、Noneならば空文字を返す

        Args:
            s (str | None): チェックする値
        """
        if type(s) is str:
            return s
        else:
            return ""
    
    def print(self):
        print(self.user_id, self.password, self.ssid_list, self.url)
