import os
from copy import deepcopy

from api.api_caller import ApiCaller
from domain.menu import Menu
import json

from menu_factory import MenuFactory

if __name__ == "__main__":

    BASE_URL = "http://localhost:8080"
    menu_api_caller = ApiCaller(BASE_URL)
    menu_api_caller.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))

    # menu_factory = MenuFactory()
    for i in range(18, 37 + 1):
        menu_api_caller.delete_menu(i)