from api.api_caller import ApiCaller
from config.config_model import ConfigManager


class MenuListPage:
    def __init__(self, window):
        self.window = window
        self.menu_list = []
        config = ConfigManager.load_config()
        self.api = ApiCaller(config.base_url)
