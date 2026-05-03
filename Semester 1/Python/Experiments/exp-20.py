class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name}: Rs {self.price} x {self.quantity}"
    
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]
    def total_cost(self):
        return sum(item.price * item.quantity for item in self.items)
    def __str__(self):
        return "\n".join(str(item) for item in self.items) + f"\nTotal: Rs {self.total_cost():.2f}"
    
cart = ShoppingCart()
cart.add_item(Item("Apple", 2, 4))
cart.add_item(Item("Banana", 5, 10))
cart.remove_item("Apple")
print(cart)