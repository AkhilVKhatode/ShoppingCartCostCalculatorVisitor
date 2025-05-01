# Shopping Cart Visitor Pattern Implementation

A Python implementation of the Visitor design pattern for a shopping cart system that handles different item types with various operations.

## Overview

This project demonstrates how to use the Visitor pattern to:
- Separate algorithms from the objects on which they operate
- Add new operations without modifying existing classes
- Handle different types of shopping cart items (books, electronics, groceries) with different business rules

## Design Pattern: Visitor

The Visitor pattern is a behavioral design pattern that lets you separate algorithms from the objects on which they operate. This is particularly useful when you need to perform various operations on a set of objects with different classes.

## Key Components

1. **Visitors** (Operations):
   - `DiscountVisitor`: Calculates discounts for different item types
   - `TaxVisitor`: Computes taxes based on item categories
   - `ShippingVisitor`: Estimates shipping costs

2. **Elements** (Items):
   - `Book`: Represents book items with title and price
   - `Electronics`: Represents electronic items with name, price, and weight
   - `Groceries`: Represents grocery items with name, price, and perishable flag

3. **Shopping Cart**:
   - Manages a collection of items
   - Applies visitors to calculate totals for different operations

## How It Works

1. Each item type implements the `accept()` method which calls the appropriate visitor method
2. Visitors implement specific operations for each item type
3. The shopping cart can apply any visitor to all items to calculate totals

## Usage Example

```python
# Create items
book = Book("Design Patterns", 49.99)
laptop = Electronics("Laptop", 999.99, 3.5)
milk = Groceries("Organic Milk", 4.99, True)

# Create cart and add items
cart = ShoppingCart()
cart.add_item(book)
cart.add_item(laptop)
cart.add_item(milk)

# Calculate discounts
discount = cart.calculate_total(DiscountVisitor())
print(f"Total Discount: ${discount:.2f}")

# Calculate taxes
tax = cart.calculate_total(TaxVisitor())
print(f"Total Tax: ${tax:.2f}")

# Calculate shipping
shipping = cart.calculate_total(ShippingVisitor())
print(f"Total Shipping: ${shipping:.2f}")
```

## Benefits of This Implementation
- Extensible: Easy to add new operations (visitors) without modifying existing classes
- Maintainable: Business rules for each item type are encapsulated in visitors
- Flexible: New item types can be added with minimal changes to existing code
