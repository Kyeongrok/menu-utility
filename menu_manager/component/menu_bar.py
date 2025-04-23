import tkinter as tk
from tkinter import messagebox


class MenuBar(tk.Menu):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        # Create File menu
        file_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Refresh", command=parent.load_data)
        file_menu.add_command(label="Export to Excel")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=parent.quit)

        # Create PLC Tags menu
        tag_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="PLC Tags", menu=tag_menu)
        tag_menu.add_command(label="View Tags")
        tag_menu.add_command(label="Add New Tag")

        # Create Help menu
        help_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About",
                              command=lambda: messagebox.showinfo("About", "PLC Monitoring Tool v1.0"))


