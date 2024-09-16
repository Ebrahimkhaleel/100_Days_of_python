
#A dictionary to store products
products = {
    "1": {"name": "Laptop", "price": 1000},
    "2": {"name": "Mobile phone", "price": 350},
    "3": {"name": "Mifi", "price": 100},
}

# A dictionary to store cart
cart = {}

def display_products():
    print("Available Products:")
    for key, value in products.items():
        print(f"{key}. {value['name']} - N{value['price']}")

def add_to_cart():
    product_id = input("Enter product ID: ")
    if product_id in products:
        if product_id in cart:
            cart[product_id]["quantity"] += 1
        else:
            cart[product_id] = {"name": products[product_id]["name"], "price": products[product_id]["price"], "quantity": 1}
        print(f"Added {products[product_id]['name']} to cart.")
    else:
        print("Invalid product ID.")

def remove_from_cart():
    product_id = input("Enter product ID: ")
    if product_id in cart:
        del cart[product_id]
        print(f"Removed {products[product_id]['name']} from cart.")
    else:
        print("Product not in cart.")

def calculate_total():
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    print(f"Total: N{total:.2f}")

def display_cart():
    print("Cart:")
    for key, value in cart.items():
        print(f"{value['name']} x {value['quantity']} - N{value['price'] * value['quantity']:.2f}")

while True:
    print("\n1. Display Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. Calculate Total")
    print("5. Display Cart")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        display_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        remove_from_cart()
    elif choice == "4":
        calculate_total()
    elif choice == "5":
        display_cart()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
