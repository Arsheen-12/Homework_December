fruits = {
    "Apple": 120,    
    "Banana": 50,    
    "Orange": 80,    
    "Grapes": 150,   
    "Mango": 100,    
    "Pineapple": 60,
    "Watermelon": 50,
    "Sweetlime": 80, 
    "Kiwi": 120,
    "Strawberry": 150
}

cart = {}

print("-------------------- Welcome to the Fruits Shop!!!! ---------------------")
while True:
    print("\n-------------- Menu -------------------------")
    print("1. View Fruits")
    print("2. Add to Cart")
    print("3. Your Cart")
    print("4. Total Bill")
    print("5. Payment")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        print("\n----- Available Fruits --------")
        for fruit, price in fruits.items():
            if fruit == "Grapes":
                print(f"{fruit}: ₹{price}/bunch")
            elif fruit in ["Kiwi", "Strawberry"]:
                print(f"{fruit}: ₹{price}/packet")
            else:
                print(f"{fruit}: ₹{price}/kg")

    elif choice == "2":
        selected_fruits = input("Enter the fruits you want to add to the cart: ").split(",")
        for fruit in selected_fruits:
            fruit = fruit.strip().capitalize()
            if fruit in fruits:
                if fruit == "Grapes":
                    qty = input(f"Enter number of bunches for {fruit}: ")
                elif fruit in ["Kiwi", "Strawberry"]:
                    qty = input(f"Enter number of packets for {fruit}: ")
                else:
                    qty = input(f"Enter quantity (in kg) for {fruit}: ")

                if qty.isdigit():
                    qty = int(qty)
                    if fruit in cart:
                        cart[fruit] += qty
                    else:
                        cart[fruit] = qty

                    unit = "bunches" if fruit == "Grapes" else "packets" if fruit in ["Kiwi", "Strawberry"] else "kg"
                    print(f"{qty} {unit} of {fruit} added to your cart.")
                else:
                    print(f"Invalid quantity for {fruit}. Please enter a numeric value.")
            else:
                print(f"{fruit} is not available in the shop.")

    elif choice == "3":
        if cart:
            print("\n--------- Your Cart Summary ------------------")
            for fruit, qty in cart.items():
                unit = "bunches" if fruit == "Grapes" else "packets" if fruit in ["Kiwi", "Strawberry"] else "kg"
                print(f"{fruit}: {qty} {unit}")
        else:
            print("Your cart is empty.")

    elif choice == "4":
        if cart:
            print("\n--------- Billing Details ------------------")
            bill_date = input("Enter the date for the bill (YYYY-MM-DD): ")
            
            print(f"Bill Date: {bill_date}")
            total = 0
            for fruit, qty in cart.items():
                subtotal = fruits[fruit] * qty
                total += subtotal
                unit = "bunches" if fruit == "Grapes" else "packets" if fruit in ["Kiwi", "Strawberry"] else "kg"
                print(f"{fruit}: {qty} {unit} x ₹{fruits[fruit]} = ₹{subtotal}")
            print(f"Total: ₹{total}")
        else:
            print("Your cart is empty.")

    elif choice == "5":
        if cart:
            print("\n--------- Payment Options ------------------")
            print("1. Cash")
            print("2. UPI")
            payment_choice = input("Select your payment method (1-2): ")

            if payment_choice == "1":
                print("Payment successful with Cash. Thank you for shopping!")
            elif payment_choice == "2":
                print("Payment successful with UPI. Thank you for shopping!")
            else:
                print("Invalid payment method selected.")
        else:
            print("Your cart is empty. Please add items to proceed to payment.")

    elif choice == "6":
        print("Thank you for visiting the Fruits Shop! Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
