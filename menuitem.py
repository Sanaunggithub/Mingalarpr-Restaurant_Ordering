from abc import ABC,abstractmethod

class MenuItem(ABC):
    def __init__(self, name, price, image_path):
        self.name = name
        self.price = price
        self.image_path = image_path
        
    @abstractmethod
    def display(self):
        pass


class Dish(MenuItem):
    def __init__(self, name, price, image_path):
        super().__init__(name, price, image_path)

    def display(self):
        return self.name, self.image_path, self.price

class Beverage(MenuItem):
    def __init__(self, name, price, image_path):
        super().__init__(name, price, image_path)

    def display(self):
        return self.name, self.image_path, self.price

class DishNotSelectedError(Exception):
    def __init__(self, message="Please select a dish before adding to the order."):
        self.message = message
        super().__init__(self.message)