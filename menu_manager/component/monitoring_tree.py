import tkinter as tk
from tkinter import ttk

class MonitoringTree(ttk.Frame):
    def __init__(self, parent, column_config, on_double_click, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Create Treeview with columns from configuration
        self.tree = ttk.Treeview(self, columns=tuple(column_config.keys()), show="headings")

        # Configure columns based on configuration
        for col, config in column_config.items():
            self.tree.heading(col, text=config['text'])
            self.tree.column(col, width=config['width'])

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Pack widgets
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind double click event
        self.tree.bind('<Double-1>', on_double_click)

    def insert_data(self, data):
        # Clear existing items
        self.clear()

        # Insert data into treeview
        for item in data:
            self.tree.insert("", tk.END, values=(
                item.logid,
                item.message_type,
                item.deviceid,
                item.company_code,
                item.send_datetime,
                item.message_version,
                f"{item.type}{item.address}",
                item.value
            ))

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_selected_values(self):
        selected_item = self.tree.selection()[0]
        return self.tree.item(selected_item)['values']