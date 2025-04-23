import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from menu_manager.models.plc_tag import PlcTag

class TagListWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("PLC Tag List")
        self.geometry("800x400")
        
        # Create main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create Treeview
        self.tree = ttk.Treeview(main_frame, columns=(
            "id", "company_code", "tag_name", "address", 
            "unit", "data_type", "description", "is_active"
        ), show="headings")

        # Define headings
        self.tree.heading("id", text="ID")
        self.tree.heading("company_code", text="Company")
        self.tree.heading("tag_name", text="Tag Name")
        self.tree.heading("address", text="Address")
        self.tree.heading("unit", text="Unit")
        self.tree.heading("data_type", text="Data Type")
        self.tree.heading("description", text="Description")
        self.tree.heading("is_active", text="Active")

        # Configure columns
        self.tree.column("id", width=50)
        self.tree.column("company_code", width=80)
        self.tree.column("tag_name", width=150)
        self.tree.column("address", width=80)
        self.tree.column("unit", width=80)
        self.tree.column("data_type", width=80)
        self.tree.column("description", width=200)
        self.tree.column("is_active", width=60)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Button frame
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(button_frame, text="Add New", command=self.add_tag).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Edit", command=self.edit_tag).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Delete", command=self.delete_tag).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Refresh", command=self.load_data).pack(side=tk.LEFT, padx=5)

        # Pack Treeview and scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Load initial data
        self.load_data()

    def load_data(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Create database connection
        engine = create_engine('sqlite:///c:/Users/Administrator/git/python/plc/plc_monitoring.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            tags = session.query(PlcTag).all()
            for tag in tags:
                self.tree.insert("", tk.END, values=(
                    tag.id,
                    tag.company_code,
                    tag.tag_name,
                    tag.address,
                    tag.unit,
                    tag.data_type,
                    tag.description,
                    "Yes" if tag.is_active else "No"
                ))
        finally:
            session.close()

    def add_tag(self):
        from gui.windows.tag_form_window import TagFormWindow
        TagFormWindow(self, None, self.load_data)

    def edit_tag(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a tag to edit")
            return
        
        tag_id = self.tree.item(selected[0])['values'][0]
        from gui.windows.tag_form_window import TagFormWindow
        TagFormWindow(self, tag_id, self.load_data)

    def delete_tag(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a tag to delete")
            return
        
        if not messagebox.askyesno("Confirm", "Are you sure you want to delete this tag?"):
            return

        tag_id = self.tree.item(selected[0])['values'][0]
        engine = create_engine('sqlite:///c:/Users/Administrator/git/python/plc/plc_monitoring.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            tag = session.query(PlcTag).filter_by(id=tag_id).first()
            if tag:
                session.delete(tag)
                session.commit()
                self.load_data()
        finally:
            session.close()