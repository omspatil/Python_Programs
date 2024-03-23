def Generate_bill():
    total_cost = 0
    menu = {
        "Masala Dosa": 60,
        "Plan dosa": 50,
        "Vada Sambar": 50,
        "Idli Sambar": 50,
        "Uttappa": 50,
        "Rice": 40
    }
    print("Welcome to the Restaurant!")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: {price}")


    while True:
            item = input("Enter item name (or 'q' to quit): ")

            if item.lower() == 'q':
                break
            if item not in menu:
                print("Invalid item. Please choose from the menu.")
                continue
            quantity = int(input("Enter quantity: "))
            cost = menu[item] * quantity
            total_cost += cost
            print(f"{quantity} {item}(s) added to the order. Cost: {cost:.2f}")
            print(f"Total cost: {total_cost:.2f}")
    with open("order_history.txt", "a") as f:
            f.write(f"Order: {', '.join([f'{quantity} {item}' for item, quantity in menu.items()])}\n")
            f.write(f"Total cost: {total_cost:.2f}\n")
            f.write("-------------------------------\n")


"""def View_Menu():
    d1 = "101,Masala Dosa,60"
    d2 = "102,Plain Dosa,50"
    d3 = "103,Vada Sambar,50"
    d4 = "104,Idli Sambar,50"
    d5 = "105,Uttappa,50"
    d6 = "106,Rice,40"
    d7 = "107,Paneer Masala,120"
    d8 = "108,Palak Paneer,120"
    d9 = "109,Chapati,12"
    d10 = "110,Papad,20"
    fobj = open("all_dish.txt", "a")
    fobj.write(
        d1 + "\n" + d2 + "\n" + d3 + "\n" + d4 + "\n" + d5 + "\n" + d6 + "\n" + d7 + "\n" + d8 + "\n" + d9 + "\n" + d10)
    fobj.close()
    print("101. Masala Dosa    -60", "\n", "102. Plain Dosa    -50", "\n", "103. Vada Sambar   -50", "\n",
          "104. Idli Sambar    -50", "\n", "105. Uttappa        -50", "\n", "106. Rice           -40", "\n",
          "107. Paneer Masala  -120", "\n", "108. Palak Paneer   -120", "\n", "109. Chapati         -12", "\n",
          "110. Papad           -20")

"""
def update_price():
    pass


def View_todays_bill_total_collection():
    pass


def view_bills_total_collectio():
    pass


print("Select your choice ")
print("1. Generate bil")
print("2. View Menue ")
print("3.Update Price")
print("4.View todays bill + Total bill")
print("5. View bills + total collection")
print("6. Exit ")
ch = int(input("Select your choice :"))
if ch == 1:
    Generate_bill()
#elif ch == 2:
    #View_Menu()
elif ch == 3:
    update_price()
elif ch == 4:
    View_todays_bill_total_collection()
elif ch == 5:
    view_bills_total_collectio()