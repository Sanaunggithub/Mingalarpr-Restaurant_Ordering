import random
import string
from tkinter import ttk, Toplevel, Canvas, Scrollbar
from datetime import datetime

class OrderConfirm:
    def __init__(self, window, items, prices_list, item_count, total_price):
        # Apply styling
        s = ttk.Style()
        s.configure('Toplevel', background='#352e29')
        s.configure('mainframe.TFrame', background='#352e29')
        s.configure('TLabel', background='#352e29', foreground='#f5e8c7', font=("Courier", 12))

        # Window Configuration
        self.window = Toplevel(window)
        self.window.title("Receipt")
        self.window.resizable(False, True)

        #Frame
        mainframe = ttk.Frame(self.window, style='mainframe.TFrame', padding=(20, 20))
        mainframe.grid(row=0, column=0, sticky='NSEW')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Generate Order ID with random letters and numbers
        order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # 8 characters

        # Current date and time for the order
        order_time = datetime.now().strftime('%I:%M %p')

        # Welcome and Receipt Header
        ttk.Label(mainframe, text="Welcome to Mingalarpr", font=("Times", 14, 'bold'), anchor='center').grid(row=0, column=0, columnspan=2, sticky='EW', pady=(5, 5))
        ttk.Label(mainframe, text="Receipt", font=("Times", 18, 'bold'), anchor='center').grid(row=1, column=0, columnspan=2, sticky='EW', pady=(5, 10))

        # Order ID and Date/Time
        ttk.Label(mainframe, text=f"Order ID: {order_id}", font=("Courier", 12)).grid(row=2, column=0, columnspan=2, sticky='EW', pady=(5, 5))
        ttk.Label(mainframe, text=f"Date: {datetime.today().strftime('%x')}  Time: {order_time}", font=("Courier", 12)).grid(row=3, column=0, columnspan=2, sticky='EW', pady=(5, 10))

        #Items and Price header
        ttk.Label(mainframe, text="Items & Price", font=("Courier", 12, 'bold')).grid(row=4, column=0, sticky='W')

        # Canvas for scrollable items and prices
        canvas = Canvas(mainframe, background='#352e29', highlightthickness=0)
        canvas.grid(row=5, column=0, columnspan=2, sticky='NSEW', padx=(10, 10), pady=(5, 10))

        # Scrollbar configuration
        scrollbar = Scrollbar(mainframe, orient="vertical", command=canvas.yview, background='#704214', troughcolor='#352e29', activebackground='#f5e8c7')
        scrollbar.grid(row=5, column=2, sticky='NS', padx=(0, 10))
        canvas.configure(yscrollcommand=scrollbar.set)

        # Inner frame in canvas to hold items and prices
        scrollable_frame = ttk.Frame(canvas, style='mainframe.TFrame')
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Update canvas scroll region when items are added
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Display Items and Prices
        for i, item in enumerate(items):
            quantity = item_count[item]
            price = prices_list[i] * quantity
            ttk.Label(scrollable_frame, text=f"{item} x{quantity}", background='#352e29', foreground='#f5e8c7', font=("Courier", 12)).grid(row=i, column=0, sticky='W', padx=5, pady=(5, 5))
            ttk.Label(scrollable_frame, text=f"${price:.2f}", background='#352e29', foreground='#f5e8c7', font=("Courier", 12)).grid(row=i, column=1, sticky='E', padx=5, pady=(5, 5))

        # Total Price
        ttk.Label(mainframe, text=f"Total: ${total_price:.2f}", font=("Courier", 14, 'bold')).grid(row=6, column=0, columnspan=2, sticky='EW', pady=(10, 5))

        # Close Button
        ttk.Button(mainframe, text="Close", command=self.window.destroy).grid(row=7, column=0, columnspan=2, pady=(10, 5))

        # Thank You Message
        ttk.Label(mainframe, text="Thank You!!!", font=("Courier", 16, 'italic'), anchor='center').grid(row=8, column=0, columnspan=2, sticky='EW', pady=(15, 5))

        # Configuration
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_rowconfigure(8, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)