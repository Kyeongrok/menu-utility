import tkinter as tk
from tkinter import messagebox

class MenuBar(tk.Menu):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Create File menu
        file_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Refresh", command=parent.load_data)
        file_menu.add_command(label="Export to Excel", command=lambda: self.export_to_excel())
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=parent.quit)
        

        # Create PLC Tags menu
        tag_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="PLC Tags", menu=tag_menu)
        tag_menu.add_command(label="View Tags", command=lambda: self.show_tag_list())
        tag_menu.add_command(label="Add New Tag", command=lambda: self.show_tag_form())

        # Create PLC Alert menu
        alert_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="PLC Alert", menu=alert_menu)
        alert_menu.add_command(label="View Alerts", command=lambda: self.show_alert_list())
        alert_menu.add_command(label="Configure Alerts", command=lambda: self.show_alert_config())

        # Create Help menu
        help_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", 
            command=lambda: messagebox.showinfo("About", "PLC Monitoring Tool v1.0"))

    def show_tag_list(self):
        # This will be implemented in a separate TagListWindow class
        from menu_manager.gui.windows.tag_list_window import TagListWindow
        TagListWindow(self)

    def show_tag_form(self, tag=None):
        # This will be implemented in a separate TagFormWindow class
        from menu_manager.gui.windows.tag_form_window import TagFormWindow
        TagFormWindow(self, tag)

    def export_to_excel(self):
        from tkinter import filedialog
        import pandas as pd
        
        # Get file path from user
        file_path = filedialog.asksaveasfilename(
            defaultextension='.xlsx',
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                # Get data from parent's tree
                data = []
                for item in self.master.tree.get_children():
                    data.append(self.master.tree.item(item)['values'])
                
                # Create DataFrame
                columns = [self.master.tree.heading(col)['text'] for col in self.master.tree['columns']]
                df = pd.DataFrame(data, columns=columns)
                
                # Export to Excel
                df.to_excel(file_path, index=False)
                messagebox.showinfo("Success", "Data exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export data: {str(e)}")