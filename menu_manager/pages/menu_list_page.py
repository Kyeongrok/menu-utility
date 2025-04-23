from tkinter import Frame, Label

from api.api_caller import ApiCaller
from config.config_model import ConfigManager
from cookie.cookie_manager import CookieManager
from style import FONTS


class MenuListPage:
    def __init__(self, window):
        config = ConfigManager.load_config()
        self.cookie_manager = CookieManager()
        self.window = window
        self.menu_list = []
        self.api = ApiCaller(config.base_url)

    def create_page(self, parent):

        content_area = Frame(self.window, bg="white")
        content_area.pack(side="left", fill="both", expand=True)

        Label(content_area, text="메뉴 관리 시스템", font=FONTS["title1"], bg="white",
              anchor="w").pack(fill="x", padx=20, pady=(10, 0))





