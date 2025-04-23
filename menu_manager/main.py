import os

from api.api_caller import ApiCaller
from gui.monitoring_view import MonitoringView


if __name__ == "__main__":

    BASE_URL = "http://localhost:8080"
    menu_api_caller = ApiCaller(BASE_URL)
    # menu_api_caller.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))

    app = MonitoringView()
    app.mainloop()
