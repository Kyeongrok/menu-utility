from tkinter import Tk, Frame, Label
from style import FONTS, COLORS
from pages.main_page import MainPage


def init_gui():
    window = Tk()

    window.title("메뉴 관리 시스템")
    window.geometry("1400x800")

    # header
    header_frame = Frame(window, bg="#1976D2", height=50)  # Material Design Blue
    header_frame.pack(fill="x")

    # Header 텍스트 (좌측)
    header_label = Label(
        header_frame,
        text="메뉴 관리 앱",
        font=("Malgun Gothic", 16, "bold"),
        fg="#FFFFFF",
        bg="#1976D2",  # Match with header frame
        anchor="w",
        padx=30,
        pady=12,
    )
    header_label.pack(side="left", fill="y", padx=(10, 0))  # Add left margin


    # Content Area
    main_frame = Frame(window, bg="white")
    main_frame.pack(fill="both", expand=True)

    # Create main page
    MainPage(main_frame, "http://localhost:8080").create_main_page(main_frame)

    window.mainloop()


if __name__ == "__main__":
    init_gui()
