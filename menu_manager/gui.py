from tkinter import Tk, Frame, Label
from pages.login_page import LoginPage
from component.menu_bar import MenuBar


def init_gui():
    window = Tk()

    window.title("메뉴 관리 시스템")
    window.geometry("1400x800")

    # Add menu bar
    MenuBar(window)

    # Content Area
    main_frame = Frame(window, bg="white")
    main_frame.pack(fill="both", expand=True)

    LoginPage(main_frame, "http://localhost:8080").create_main_page(main_frame)

    window.mainloop()


if __name__ == "__main__":
    init_gui()
