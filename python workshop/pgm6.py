
products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
            "Mouse", "Monitor", "Printer", "Charger", "Camera"]

print("Initial Products List:")
print(products)


products.append("Smartwatch")
print("\nAfter Appending 'Smartwatch':")
print(products)


products.remove("Tablet")
print("\nAfter Removing 'Tablet':")
print(products)


products[3] = "Bluetooth Headphones"  
print("\nAfter Updating 'Headphones' to 'Bluetooth Headphones':")
print(products)
