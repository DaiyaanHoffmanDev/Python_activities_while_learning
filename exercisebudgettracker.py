# shopping list

name = input("Enter your name: ")
monthly_budjet = float(input("Enter your monthly budjet: R"))
shopping_list =  []



while not shopping_list == "done":
    items = input("enter an item to purchase: ")
    if items == "done":
        print("bye")
        break
    else:
        prices = float(input("Enter the prices of the item: R"))
        monthly_budjet = monthly_budjet - prices
        shopping_list.append(items)
        print(f"you have purchased{shopping_list} type (done) to end")

if monthly_budjet == 0:
    print("You are broke")
elif monthly_budjet < 0:
    print("you are in dept")
else:
    print(f"you have R{monthly_budjet} left")

for i in shopping_list:
    print(f"You have purchased {i}")