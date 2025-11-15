from tkinter import Toplevel, ttk, Canvas, Scrollbar
import tkinter.messagebox
from orderconfirm import *

class Add:
    def __init__(self, window):
        s = ttk.Style()
        s.configure('Buttons.TFrame', background='#493628')
        s.configure('label.TFrame', background='#493628')

        self.window = Toplevel(window, background='#493628')
        self.window.title("Order")
        self.window.resizable(False, False)

        self.items = []
        self.prices_list = []
        self.item_count = {}
        self.total_price = 0

        self.prices = {
            "mohinga": 50, "mhote-ti": 40, "shan-noodle": 50,
            "lat-phat-thoke": 48, "nan-gyi-thoke": 50, "ohnno": 50,
            "shan-hta-min": 50, "tofu-thoke": 45,"kat-kyi-kaik": 50,
            "coconut rice": 50, "tofu-nway": 48, "myee-shay": 49, 
            "shwe-yin-aye": 48, "mote-lone-yay-paw": 42, "tagu": 38,
            "shwe-kyi": 45, "htoe-mont": 46, "kyauk-kyaw": 48,
            "tea": 40, "pha-lu-dar": 50, "domino": 50,
            "kyan-yay": 35, "mote-lin-mayar": 50, "e-kyar-kway": 30
        }

        # Order Page Title
        ttk.Label(self.window, text="Order Page", background='#493628', foreground='#f5e8c7', anchor='center', font=("Courier", 20)).grid(row=0, column=0, columnspan=3, sticky="EW")

        # Items and Price headers
        ttk.Label(self.window, text="Items & Price", background='black', foreground='#f5e8c7', font=("Courier", 12), anchor='center').grid(row=1, column=0, sticky='EW', padx=10, pady=(10, 5))

        # Main canvas to hold items and prices frames with a shared scrollbar
        self.main_canvas = Canvas(self.window, background='#493628', highlightthickness=0)
        self.main_canvas.grid(row=2, column=0, columnspan=2, sticky='NSEW', padx=(10, 10), pady=(5, 10))

        # Scrollbar configuration
        scrollbar = Scrollbar(self.window, orient="vertical", command=self.main_canvas.yview, background='#704214', troughcolor='#493628', activebackground='#f5e8c7')
        scrollbar.grid(row=2, column=2, sticky='NS')
        self.main_canvas.configure(yscrollcommand=scrollbar.set) #Link Canvas to Scrollbar

        # Frame inside the canvas for items and prices
        self.content_frame = ttk.Frame(self.main_canvas, style="label.TFrame")
        self.main_canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Bind the scroll region to content updates
        self.content_frame.bind("<Configure>", lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))

        # Total price label
        self.total_label = ttk.Label(self.window, text=f"Total: ${self.total_price}", background='black', foreground='#f5e8c7', font=("Courier", 12), anchor='center')
        self.total_label.grid(row=3, column=0, columnspan=2, sticky='EW', padx=10, pady=(10, 5))

        # Buttons frame
        buttons = ttk.Frame(self.window, style='Buttons.TFrame')
        buttons.grid(row=4, column=0, columnspan=2, sticky='EW', padx=10, pady=(10, 15))

        buttons.columnconfigure(0, weight=1)
        buttons.columnconfigure(1, weight=1)
        buttons.columnconfigure(2, weight=1)

        ttk.Button(buttons, text="Order", command=self.confirm_order).grid(row=0, column=0, padx=10, pady=15, sticky="W")
        ttk.Button(buttons, text="Cancel", command=self.cancel_order).grid(row=0, column=2, padx=10, pady=15, sticky="W")

    def add_item(self, item_name, price):
        item_name = item_name.lower()
        if item_name in self.item_count:
            self.item_count[item_name] += 1
        else:
            self.items.append(item_name)
            self.prices_list.append(price)
            self.item_count[item_name] = 1

        self.total_price += price
        self.update_order()

    def remove_item(self, item_name):
        item_name = item_name.lower()
        if item_name in self.item_count:
            if self.item_count[item_name] > 1:
                self.item_count[item_name] -= 1
                self.total_price -= self.prices[item_name]
            else:
                index = self.items.index(item_name)
                price_to_remove = self.prices_list.pop(index)
                self.items.pop(index)
                self.total_price -= price_to_remove
                del self.item_count[item_name]

            self.update_order()
        else:
            tkinter.messagebox.showwarning("Warning", f"Item '{item_name}' is not in the order.")

    def update_order(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        for i, item in enumerate(self.items):
            quantity = self.item_count[item]
            ttk.Label(self.content_frame, text=f"{item} x{quantity}", background='#493628', foreground='#f5e8c7', font=("Courier", 12)).grid(row=i, column=0, sticky='EW', padx=5, pady=(5, 5))
            ttk.Label(self.content_frame, text=f"${self.prices_list[i] * quantity}", background='#493628', foreground='#f5e8c7', font=("Courier", 12)).grid(row=i, column=1, sticky='EW', padx=5, pady=(5, 5))

        self.total_label.config(text=f"Total: {self.total_price}")

    def confirm_order(self):
        OrderConfirm(self.window, self.items, self.prices_list, self.item_count, self.total_price)

    def cancel_order(self):
        self.window.destroy()