from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox
from orderadd import Add
from menuitem import Dish, Beverage


order_window = None
selected_item = None


class DishNotSelectedError(Exception):
    def __init__(self, message="Please select a dish first."):
        self.message = message
        super().__init__(self.message)


def mingalarpr():
    window = Tk()
    window.title("Mingalarpr")
    window.geometry("800x500") 
    window.resizable(FALSE,FALSE)

    def add_to_order():
        global order_window, selected_item

        try:
            if selected_item is None:
                raise DishNotSelectedError()

            if order_window is None or not order_window.window.winfo_exists():
                order_window = Add(window)
            order_window.add_item(selected_item.name, selected_item.price)

        except DishNotSelectedError as e:
            tkinter.messagebox.showwarning("Warning", e.message)

    def remove_item_from_order():
        global selected_item
        if selected_item:
            order_window.remove_item(selected_item.name)
        else:
            tkinter.messagebox.showwarning("Warning", "No dish selected")

    def display_dish(menu_item: Dish):
        global selected_item

        # Update selected dish or beverage
        selected_item = menu_item

        # Display the dish image
        dish_image = Image.open(menu_item.image_path).resize((400, 300))
        dish_tk = ImageTk.PhotoImage(dish_image)
        image_label.config(image=dish_tk)
        image_label.image = dish_tk

        # Update the price label
        price_label.config(text=f"Price: ${menu_item.price}")
        price_label.grid()  # Show the price label

    # Style configuration
    s = ttk.Style()
    s.configure('mainframe.TFrame', background='#352e29')
    s.configure('menuframe.TFrame', background=' #AB886D')
    s.configure('displayframe.TFrame', background='#352e29')
    s.configure('beverage.TFrame', background='#AB886D', font='Courier')
    s.configure('display.TButton', background='#AB886D', foreground='black', padding=5, font='Courier', relief=RAISED)

    # Frames
    mainframe = ttk.Frame(window, style='mainframe.TFrame')
    mainframe.grid(row=0, column=0, sticky="NSEW", padx=10, pady=5)

    menuframe = ttk.Frame(mainframe, style='menuframe.TFrame')
    menuframe.grid(row=1, column=0, padx=3, pady=3, sticky='NESW')

    beverageframe = ttk.Frame(mainframe, style='beverage.TFrame')
    beverageframe.grid(row=1, column=1, padx=3, pady=3, sticky='NESW')

    displayframe = ttk.Frame(mainframe, style='displayframe.TFrame')
    displayframe.grid(row=1, column=2, padx=3, pady=3, sticky='EW')

    # Add, Remove buttons
    add_button = ttk.Button(displayframe, text="Add to order", command=add_to_order)
    add_button.grid(row=3, column=0, sticky='W', padx=5, pady=3)
    remove_button = ttk.Button(displayframe, text="Remove", command=remove_item_from_order)
    remove_button.grid(row=3, column=0, sticky='E', padx=5, pady=3)

    # Mingalarpr Heading
    ttk.Label(mainframe, text="Mingalarpr", background='#352e29', foreground='#f5e8c7', anchor='center', font=("Times", 20)).grid(row=0, column=1, sticky="EW")

    # Menu title
    ttk.Label(menuframe, text="Meals", background='black', foreground='#f5e8c7', anchor='center', font=("Courier",13)).grid(row=0, column=0, sticky="EW")

    #beverage & Dessert title
    ttk.Label(beverageframe, text="Beverage & Dessert",background='black', foreground='#f5e8c7',anchor='center',font=("Courier",13)).grid(row=0,column=0,sticky="EW")

    #Order here title
    ttk.Label(displayframe, text= "ORDER HERE!", background='#352e29', foreground='#f5e8c7',anchor='center',font=('Courier',15,'italic')).grid(row=0,column=0)

    # Default image
    try:
        restaurant_origin = Image.open('menu/restauarant.jpg').resize((400, 300))
        restauranttk = ImageTk.PhotoImage(restaurant_origin)
        image_label = Label(displayframe, image=restauranttk, anchor='center')
        image_label.grid(row=1, column=0, sticky='NESW')
        image_label.image = restauranttk
        
    except Exception as e:
        tkinter.messagebox.showerror("Error", f"Failed to load restaurant image: {e}")

    # Menu items
    mohinga = Dish("Mohinga", 50, 'menu/mohinga.jpg')
    mohinga_button = ttk.Button(menuframe, text="Mohinga", style="display.TButton", command=lambda: display_dish(mohinga))
    mohinga_button.grid(row=1, column=0, sticky='EW')

    mhoteti = Dish("Mhote-ti", 40, 'menu/mhoteti.gif')
    mhoteti_button = ttk.Button(menuframe, text="Mhote-ti", style="display.TButton", command=lambda: display_dish(mhoteti))
    mhoteti_button.grid(row=2, column=0, sticky='EW')

    shannoodle = Dish("Shan-noodle", 50, 'menu/shannoodle.gif')
    shannoodle_button = ttk.Button(menuframe, text="Shan-noodle", style="display.TButton", command=lambda: display_dish(shannoodle))
    shannoodle_button.grid(row=3, column=0, sticky='EW')

    latphatthoke = Dish("Lat-phat-thoke", 48, 'menu/latphat.jpg')
    latphatthoke_button = ttk.Button(menuframe, text="Lat-phat-thoke", style="display.TButton", command=lambda: display_dish(latphatthoke))
    latphatthoke_button.grid(row=4, column=0, sticky='EW')

    nangyithoke = Dish("Nan-gyi-thoke", 50, 'menu/nangyithoke.gif')
    nangyithoke_button = ttk.Button(menuframe, text="Nan-gyi-thoke", style="display.TButton", command=lambda: display_dish(nangyithoke))
    nangyithoke_button.grid(row=5, column=0, sticky='EW')

    ohnno = Dish("Ohnno", 50, 'menu/ohnno.gif')
    ohnno_button = ttk.Button(menuframe, text="Ohnno", style="display.TButton", command=lambda: display_dish(ohnno))
    ohnno_button.grid(row=6, column=0, sticky='EW')

    shanhtamin = Dish("Shan-Hta-Min", 50, 'menu/shanhtamin.gif')
    shanhtamin_button = ttk.Button(menuframe, text="Shan-Hta-Min", style="display.TButton", command=lambda: display_dish(shanhtamin))
    shanhtamin_button.grid(row=7, column=0, sticky='EW')

    tofuthoke = Dish("Tofu-thoke", 45, 'menu/tofuthoke.gif')
    tofuthoke_button = ttk.Button(menuframe, text="Tofu-thoke", style="display.TButton", command=lambda: display_dish(tofuthoke))
    tofuthoke_button.grid(row=8, column=0, sticky='EW')

    katkyikaik = Dish("Kat-kyi-kaik", 50, 'menu/kat-kyi-kaik2.jpg')
    katkyikaik_button = ttk.Button(menuframe, text="Kat-kyi-kaik", style="display.TButton", command=lambda: display_dish(katkyikaik))
    katkyikaik_button.grid(row=9, column=0, sticky='EW')

    coconutrice = Dish("Coconut rice", 50, 'menu/coconutrice.gif')
    coconutrice_button = ttk.Button(menuframe, text="Coconut rice", style="display.TButton", command=lambda: display_dish(coconutrice))
    coconutrice_button.grid(row=10, column=0, sticky='EW')

    tofunway = Dish("Tofu-nway", 48, 'menu/tofunway.gif')
    tofunway_button = ttk.Button(menuframe, text="Tofu-nway", style="display.TButton", command=lambda: display_dish(tofunway))
    tofunway_button.grid(row=11, column=0, sticky='EW')

    myeeshay = Dish("Myee-shay", 49, 'menu/myeeshay.gif')
    myeeshay_button = ttk.Button(menuframe, text="Myee-shay", style="display.TButton", command=lambda: display_dish(myeeshay))
    myeeshay_button.grid(row=12, column=0, sticky='EW')

    # Beverage Items
    shweyinaye = Beverage("Shwe-yin-aye", 48, 'menu/shweyinaye.jpg')
    shweyinaye_button = ttk.Button(beverageframe, text="Shwe-yin-aye", style="display.TButton", command=lambda: display_dish(shweyinaye))
    shweyinaye_button.grid(row=1, column=0, sticky='EW')

    montloneyaypaw = Beverage("Mote-lone-yay-paw", 42, 'menu/montloneyaypaw.jpg')
    montloneyaypaw_button = ttk.Button(beverageframe, text="Mote-lone-yay-paw", style="display.TButton", command=lambda: display_dish(montloneyaypaw))
    montloneyaypaw_button.grid(row=2, column=0, sticky='EW')

    tagu = Beverage("Tagu", 38, 'menu/tagu.gif')
    tagu_button = ttk.Button(beverageframe, text="Tagu", style="display.TButton", command=lambda: display_dish(tagu))
    tagu_button.grid(row=3, column=0, sticky='EW')

    shwekyi = Beverage("Shwe-kyi", 45, 'menu/shwekyi.jpg')
    shwekyi_button = ttk.Button(beverageframe, text="Shwe-kyi", style="display.TButton", command=lambda: display_dish(shwekyi))
    shwekyi_button.grid(row=4, column=0, sticky='EW')

    htoemont = Beverage("Htoe-mont", 46, 'menu/htoemont.jpg')
    htoemont_button = ttk.Button(beverageframe, text="Htoe-mont", style="display.TButton", command=lambda: display_dish(htoemont))
    htoemont_button.grid(row=5, column=0, sticky='EW')

    kyaukkyaw = Beverage("Kyauk-kyaw", 48, 'menu/kyautkyaw.jpg')
    kyaukkyaw_button = ttk.Button(beverageframe, text="Kyauk-kyaw", style="display.TButton", command=lambda: display_dish(kyaukkyaw))
    kyaukkyaw_button.grid(row=6, column=0, sticky='EW')

    tea = Beverage("Tea", 40, 'menu/tea.jpg')
    tea_button = ttk.Button(beverageframe, text="Tea", style="display.TButton", command=lambda: display_dish(tea))
    tea_button.grid(row=7, column=0, sticky='EW')

    phaludar = Beverage("Pha-lu-dar", 50, 'menu/phaludar.jpeg')
    phaludar_button = ttk.Button(beverageframe, text="Pha-lu-dar", style="display.TButton", command=lambda: display_dish(phaludar))
    phaludar_button.grid(row=8, column=0, sticky='EW')

    domino = Beverage("Domino", 50, 'menu/domino.jpg')
    domino_button = ttk.Button(beverageframe, text="Domino", style="display.TButton", command=lambda: display_dish(domino))
    domino_button.grid(row=9, column=0, sticky='EW')

    kyanyay = Beverage("Kyan-yay", 35, 'menu/kyanyay.gif')
    kyanyay_button = ttk.Button(beverageframe, text="Kyan-yay", style="display.TButton", command=lambda: display_dish(kyanyay))
    kyanyay_button.grid(row=10, column=0, sticky='EW')

    motelinmayar = Beverage("Mote-lin-mayar", 50, 'menu/motelinmayar.jpg')
    motelinmayar_button = ttk.Button(beverageframe, text="Mote-lin-mayar", style="display.TButton", command=lambda: display_dish(motelinmayar))
    motelinmayar_button.grid(row=11, column=0, sticky='EW')

    ekyarkway = Beverage("E-kyar-kway", 30, 'menu/ekyarkway.jpg')
    ekyarkway_button = ttk.Button(beverageframe, text="E-kyar-kway", style="display.TButton", command=lambda: display_dish(ekyarkway))
    ekyarkway_button.grid(row=12, column=0, sticky='EW')                                


    #mainframe configuration
    window.rowconfigure(0,weight=1)
    window.columnconfigure(0,weight=1)

    mainframe.rowconfigure((0,1,2),weight=4)
    mainframe.columnconfigure((0,1,2),weight=4)

    #beverage configuration
    beverageframe.columnconfigure(0,weight=1)
    beverageframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
    
    #menuframe configuration
    menuframe.columnconfigure(0,weight=1)
    menuframe.rowconfigure((1,2,3,4,5,6,7,8,9,10,11,12),weight=1)

    #display configuration
    displayframe.columnconfigure(0,weight=1)
    displayframe.rowconfigure((0,1,2),weight=1)

    # Create the price label and hide it initially
    price_label = Label(displayframe, text="Price: ", anchor='center', font=("Courier", 12), background='#f5e8c7')

    # Initially hide the label
    price_label.grid(row=2, column=0, sticky='EW')
    price_label.grid_remove()  # This hides the label initially
    
    window.mainloop()

if __name__ == "__main__":
    mingalarpr()