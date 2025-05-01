from abc import ABC, abstractmethod

# Visitor Interface
class ShoppingCartVisitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass
    
    @abstractmethod
    def visit_electronics(self, electronics):
        pass
    
    @abstractmethod
    def visit_groceries(self, groceries):
        pass

# Element Interface
class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Concrete Elements
class Book(Item):
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def accept(self, visitor):
        return visitor.visit_book(self)

class Electronics(Item):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    def accept(self, visitor):
        return visitor.visit_electronics(self)

class Groceries(Item):
    def __init__(self, name, price, perishable):
        self.name = name
        self.price = price
        self.perishable = perishable
    
    def accept(self, visitor):
        return visitor.visit_groceries(self)

# Concrete Visitors
class DiscountVisitor(ShoppingCartVisitor):
    def visit_book(self, book):
        # 10% discount on books
        return book.price * 0.10
    
    def visit_electronics(self, electronics):
        # 5% discount on electronics over $100
        if electronics.price > 100:
            return electronics.price * 0.05
        return 0
    
    def visit_groceries(self, groceries):
        # No discount on groceries
        return 0

class TaxVisitor(ShoppingCartVisitor):
    def visit_book(self, book):
        # Books are tax-free
        return 0
    
    def visit_electronics(self, electronics):
        # 8% tax on electronics
        return electronics.price * 0.08
    
    def visit_groceries(self, groceries):
        # 3% tax on non-perishable groceries, 1% on perishable
        if groceries.perishable:
            return groceries.price * 0.01
        return groceries.price * 0.03

class ShippingVisitor(ShoppingCartVisitor):
    def visit_book(self, book):
        # Flat rate for books
        return 2.99
    
    def visit_electronics(self, electronics):
        # Electronics shipping based on weight
        return max(5.99, electronics.weight * 1.5)
    
    def visit_groceries(self, groceries):
        # Groceries require special shipping
        return 7.99 if groceries.perishable else 4.99

# Shopping Cart class
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def calculate_total(self, visitor):
        total = 0
        for item in self.items:
            total += item.accept(visitor)
        return total

# Usage example
if __name__ == "__main__":
    # Create some items
    book = Book("Design Patterns", 49.99)
    laptop = Electronics("Laptop", 999.99, 3.5)
    milk = Groceries("Organic Milk", 4.99, True)
    rice = Groceries("Basmati Rice", 8.99, False)
    
    # Create shopping cart and add items
    cart = ShoppingCart()
    cart.add_item(book)
    cart.add_item(laptop)
    cart.add_item(milk)
    cart.add_item(rice)
    
    # Calculate discounts
    discount_visitor = DiscountVisitor()
    total_discount = cart.calculate_total(discount_visitor)
    print(f"Total Discount: ${total_discount:.2f}")
    
    # Calculate taxes
    tax_visitor = TaxVisitor()
    total_tax = cart.calculate_total(tax_visitor)
    print(f"Total Tax: ${total_tax:.2f}")
    
    # Calculate shipping
    shipping_visitor = ShippingVisitor()
    total_shipping = cart.calculate_total(shipping_visitor)
    print(f"Total Shipping: ${total_shipping:.2f}")
    
    # Calculate total cost
    subtotal = sum(item.price for item in cart.items)
    total = subtotal - total_discount + total_tax + total_shipping
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Total: ${total:.2f}")
