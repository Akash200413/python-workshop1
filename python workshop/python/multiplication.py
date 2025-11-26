
products = ["Shirt", "Jeans", "Shoes", "Watch", "Bag",
            "Hat", "Belt", "Socks", "Wallet", "Sunglasses"]

print("Original List:", products)

# 1️⃣ Append - add new product
products.append("Perfume")
print("After Append:", products)

# 2️⃣ Remove - remove specific product
products.remove("Hat")
print("After Remove:", products)

# 3️⃣ Update - modify an existing product
products[2] = "Sports Shoes"   # updating 'Shoes'
print("After Update:", products)
