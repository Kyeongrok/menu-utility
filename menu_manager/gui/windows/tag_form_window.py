import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.plc_tag import PlcTag

class TagFormWindow(tk.Toplevel):
    def __init__(self, parent, tag_id=None, callback=None):
        super().__init__(parent)
        self.tag_id = tag_id
        self.callback = callback
        
        self.title("PLC Tag Form")
        self.geometry("400x500")

        # Create main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create form fields
        labels = ["Company Code", "Tag Name", "Address", "Unit", "Data Type", "Description"]
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(main_frame, text=label).grid(row=i, column=0, pady=5, sticky=tk.W)
            entry = ttk.Entry(main_frame, width=40)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label.lower().replace(" ", "_")] = entry

        # Add is_active checkbox
        self.is_active_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(main_frame, text="Is Active", variable=self.is_active_var).grid(
            row=len(labels), column=1, pady=10, sticky=tk.W)

        # Add buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=len(labels)+1, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="Save", command=self.save_tag).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.destroy).pack(side=tk.LEFT, padx=5)

        # Load tag data if editing
        if tag_id:
            self.load_tag_data()

    def load_tag_data(self):
        engine = create_engine('sqlite:///c:/Users/Administrator/git/python/plc/plc_monitoring.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            tag = session.query(PlcTag).filter_by(id=self.tag_id).first()
            if tag:
                self.entries['company_code'].insert(0, tag.company_code)
                self.entries['tag_name'].insert(0, tag.tag_name)
                self.entries['address'].insert(0, tag.address)
                self.entries['unit'].insert(0, tag.unit or '')
                self.entries['data_type'].insert(0, tag.data_type or '')
                self.entries['description'].insert(0, tag.description or '')
                self.is_active_var.set(tag.is_active)
        finally:
            session.close()

    def save_tag(self):
        # Validate required fields
        required = ['company_code', 'tag_name', 'address']
        for field in required:
            if not self.entries[field].get().strip():
                messagebox.showwarning("Warning", f"{field.replace('_', ' ').title()} is required")
                return

        engine = create_engine('sqlite:///c:/Users/Administrator/git/python/plc/plc_monitoring.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            if self.tag_id:
                tag = session.query(PlcTag).filter_by(id=self.tag_id).first()
            else:
                tag = PlcTag()

            tag.company_code = self.entries['company_code'].get()
            tag.tag_name = self.entries['tag_name'].get()
            tag.address = self.entries['address'].get()
            tag.unit = self.entries['unit'].get()
            tag.data_type = self.entries['data_type'].get()
            tag.description = self.entries['description'].get()
            tag.is_active = self.is_active_var.get()

            if not self.tag_id:
                session.add(tag)
            
            session.commit()
            
            if self.callback:
                self.callback()
            
            self.destroy()
            messagebox.showinfo("Success", "Tag saved successfully")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            session.close()