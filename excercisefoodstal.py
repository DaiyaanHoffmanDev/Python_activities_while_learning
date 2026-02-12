# homemade food stal 

menu = {"burger": 35,
        "hot dog": 25,
        "coke": 20,
        "curry": 45,
        "soup": 25}

total = 0
items = menu.keys()
price = menu.values()
cart = []

for items, price in menu.items():
    print(f"{items:10},R{price:.2f}")

    
while True:
    order = input("what would you like to order(q to quit)").lower()
    if order == "q":
        break
    elif not menu.get(order) is None:
        cart.append(order)
        print(f"you ordered {order}")
    else:
        print("invalid order")

for order in cart:
    total = total + menu.get(order)

    print(f"you order is {order}")
    
print()
print(f"your total is R{total}")