import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from menu_manager.models.plc_monitoring import PlcMonitoring
from menu_manager.component.menu_bar import MenuBar
from menu_manager.component.monitoring_tree import MonitoringTree

class MonitoringView(tk.Tk):
    # Define column configuration as class variable
    COLUMN_CONFIG = {
        'logid': {'text': 'Log ID', 'width': 300},
        'message_type': {'text': 'Message Type', 'width': 100},
        'deviceid': {'text': 'Device ID', 'width': 150},
        'company_code': {'text': 'Company', 'width': 100},
        'send_datetime': {'text': 'Send DateTime', 'width': 200},
        'message_version': {'text': 'Version', 'width': 80},
        'type': {'text': 'Type', 'width': 100},
        'value': {'text': 'Value', 'width': 100}
    }

    def __init__(self):
        # Enable DPI awareness
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass

        super().__init__()

        self.title("PLC Monitoring View")
        self.geometry("1400x800")  # Increased window size
        
        # Center window on screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 1400) // 2
        y = (screen_height - 800) // 2
        self.geometry(f"+{x}+{y}")
        
        # Apply modern style
        self.style = ttk.Style()
        self.style.theme_use('vista')
        
        # Configure Treeview style and row height
        self.style.configure("Treeview", rowheight=30)
        
        # Create menubar
        menubar = MenuBar(self)
        self.config(menu=menubar)

        # Create main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create monitoring tree
        self.tree = MonitoringTree(main_frame, self.COLUMN_CONFIG, self.on_double_click)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Add refresh button
        refresh_btn = ttk.Button(self, text="Refresh", command=self.load_data)
        refresh_btn.pack(pady=5)

        # Load initial data
        self.load_data()

    def load_data(self):
        # Create database connection
        engine = create_engine('sqlite:///c:/Users/Administrator/git/python/plc/plc_monitoring.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            # Fetch data from database
            monitoring_data = session.query(PlcMonitoring).all()
            # Update tree with data
            self.tree.insert_data(monitoring_data)
        finally:
            session.close()

    def on_double_click(self, event):
        values = self.tree.get_selected_values()
        
        # Create message with all values
        message = f"""Log ID: {values[0]}
Message Type: {values[1]}
Device ID: {values[2]}
Company: {values[3]}
Send DateTime: {values[4]}
Version: {values[5]}
Type: {values[6]}
Address: {values[7]}
"""
        
        # Show message box
        tk.messagebox.showinfo("Row Details", message)

if __name__ == "__main__":
    app = MonitoringView()
    app.mainloop()