from tkinter import Frame, Label, Button, Entry, StringVar

from cookie.cookie_manager import CookieManager
from style import FONTS, COLORS
from api.api_caller import ApiCaller
from utils.crypto import encrypt_text, decrypt_text

class MainPage:
    ENCRYPTION_KEY = "beautiful_rock_hello"
    
    def __init__(self, parent, base_url):
        self.parent = parent
        self.base_url = base_url
        self.cookie_manager = CookieManager()
        self.result_label = None
        self.id_var = StringVar()
        self.pw_var = StringVar()

    def handle_login(self):
        try:
            api = ApiCaller(self.base_url)
            id_value = self.id_var.get()
            pw_value = self.pw_var.get()
            result = api.login(id_value, pw_value)
            
            # Save credentials to cookie with encrypted password
            self.cookie_manager.save_cookie("last_login_id", id_value)
            encrypted_pw = encrypt_text(pw_value, self.ENCRYPTION_KEY)
            self.cookie_manager.save_cookie("last_login_pw", encrypted_pw)
            
            self.result_label.config(
                text=f"로그인 성공\n액세스 토큰: {result['result']['accessJwt'][:20]}...", 
                fg=COLORS["success"]
            )
        except Exception as e:
            self.result_label.config(text=f"로그인 실패: {str(e)}", fg=COLORS["danger"])

    def create_main_page(self, parent):
        content_area = Frame(parent, bg="white")
        content_area.pack(side="left", fill="both", expand=True)

        # Load saved credentials
        saved_id = self.cookie_manager.load_cookie("last_login_id")
        encrypted_pw = self.cookie_manager.load_cookie("last_login_pw")
        if saved_id:
            self.id_var.set(saved_id)
        if encrypted_pw:
            decrypted_pw = decrypt_text(encrypted_pw, self.ENCRYPTION_KEY)
            self.pw_var.set(decrypted_pw)

        Label(content_area, text="메뉴 관리 시스템", font=FONTS["title1"], bg="white",
            anchor="w").pack(fill="x", padx=20, pady=(10, 0))

        # Login frame with border and padding
        login_frame = Frame(content_area, bg="white", bd=1, relief="solid")
        login_frame.pack(pady=20, padx=20, ipadx=20, ipady=20)

        # ID input with grid layout
        Label(login_frame, text="아이디", bg="white", font=FONTS["button-lg"]).grid(row=0, column=0, sticky="w", pady=5)
        id_entry = Entry(login_frame, textvariable=self.id_var, font=FONTS["button-lg"], width=30)
        id_entry.grid(row=1, column=0, pady=(0, 10))

        # Password input with grid layout
        Label(login_frame, text="비밀번호", bg="white", font=FONTS["button-lg"]).grid(row=2, column=0, sticky="w", pady=5)
        pw_entry = Entry(login_frame, textvariable=self.pw_var, show="*", font=FONTS["button-lg"], width=30)
        pw_entry.grid(row=3, column=0, pady=(0, 20))

        # Result label
        self.result_label = Label(login_frame, text="", bg="white", font=FONTS["button-lg"], wraplength=400)
        self.result_label.grid(row=4, column=0, pady=10)

        login_button = Button(
            login_frame, 
            text="로그인",
            bg=COLORS["button"]["bg"],
            fg=COLORS["button"]["fg"],
            width=20,
            font=FONTS["button-lg"],
            bd=0,
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            activebackground=COLORS["button"]["hover"],
            activeforeground=COLORS["button"]["fg"],
            command=self.handle_login
        )
        login_button.grid(row=5, column=0, pady=10)

        return content_area