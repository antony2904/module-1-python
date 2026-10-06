#Inheritance – E-Commerce System

#Q1. Build a base class Product with attributes name and price.
#  Derive Electronics and Clothing classes that add warranty and size respectively.
#  Override the display() method to include these details.
#Q2. Extend the system by adding a new class Furniture (inheriting from Product) with an 
# attribute material, and override the display method.


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name} | Price: ${self.price:.2f}")


class Electronics(Product):
    def __init__(self, name: str, price: float, warranty: int):
        super().__init__(name, price)
        self.warranty = warranty  # warranty in months or years

    def display(self):
        super().display()
        print(f" -> Warranty: {self.warranty} months")


class Clothing(Product):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self.size = size

    def display(self):
        super().display()
        print(f" -> Size: {self.size}")


class Furniture(Product):
    def __init__(self, name: str, price: float, material: str):
        super().__init__(name, price)
        self.material = material

    def display(self):
        super().display()
        print(f" -> Material: {self.material}")


if __name__ == "__main__":
    laptop = Electronics("Gaming Laptop", 1299.99, warranty=24)
    shirt = Clothing("Linen Shirt", 45.50, size="L")
    chair = Furniture("Dining Chair", 150.00, material="Teak Wood")

    products = [laptop, shirt, chair]

    for item in products:
        item.display()
        print("-" * 35)