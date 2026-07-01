from dmart import dmart
class clothes(dmart):
    def __init__(self, category, product_name, price, quantity, size, color):
        super().__init__(category, product_name, price, quantity)
        self.size = size
        self.color = color

    def display_clothes_details(self):
        print(super().display_store_details())
        print(super().common_features())
        return f"colour:{self.colour}\nsize{self.size}"
