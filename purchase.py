import questionary
import datetime

def purchase(List):
    L = List
    a_name = input("Please enter your name: ")
    print(f"\nHello {a_name}! Welcome to our Electronic Store.")

    q = {}  # Purchased products

    flag = True
    while flag:
        # Prepare dropdown options
        product_names = [item[0] for item in L]
        product = questionary.select(
            "What product do you want to buy?",
            choices=product_names
        ).ask()

        product_index = next((i for i, item in enumerate(L) if item[0] == product), None)

        if product_index is not None:
            while True:
                try:
                    quantity = int(input(f"How many '{product}' do you want to buy? "))
                    if quantity <= int(L[product_index][2]):
                        q[product] = quantity
                    else:
                        print(f"Only {L[product_index][2]} units of {product} are available.")
                    break
                except ValueError:
                    print("❌ Please enter a valid number.")
        else:
            print("❌ Invalid product selection.")

        more = questionary.confirm(f"{a_name}, do you want to buy more products?").ask()
        if not more:
            flag = False

    # 🧮 Calculate total
    f_amount = 0
    product_prices = {}
    for product, quantity in q.items():
        product_index = next(i for i, item in enumerate(L) if item[0] == product)
        price = int(L[product_index][1])
        total_price = price * quantity
        product_prices[product] = total_price
        f_amount += total_price
        print(f"Total cost for {product}: {total_price}₹")

    print("\nYour discountable total amount is:", f_amount)

    # 💸 Discount Calculation
    disc = float(input("Please enter your expected discount (%): "))
    dis = 0.0

    if f_amount >= 10000:
        max_disc = 10.0
    elif f_amount >= 5000:
        max_disc = 5.0
    else:
        max_disc = 0.0

    if disc <= max_disc:
        dis = (disc * f_amount) / 100
        print(f"You got your expected {disc}% discount: {dis}₹")
    else:
        dis = (max_disc * f_amount) / 100
        print(f"Expected discount too high. Applying max allowed {max_disc}% discount: {dis}₹")

    total = f_amount - dis
    print("Your final payable amount is:", total)

    # 🧾 Generate Invoice
    now = datetime.datetime.now()
    invoice = now.strftime("%Y-%m-%d-%H-%M-%S")
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    filename = f"INVOICE {invoice} ({a_name}).txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("=============================================================\n")
        file.write("SHREYA COMPUTER & TECH ENTERPRISE\t\t\tINVOICE\n\n")
        file.write(f"Invoice: {invoice}\t\tDate: {date_str}\tTime: {time_str}\n")
        file.write(f"Name of Customer: {a_name}\n")
        file.write("=============================================================\n")
        file.write("PARTICULAR\tQUANTITY\tUNIT PRICE\tTOTAL\n")
        file.write("-------------------------------------------------------------\n")
        for product, qty in q.items():
            index = next(i for i, item in enumerate(L) if item[0] == product)
            unit_price = L[index][1]
            total_price = product_prices[product]
            file.write(f"{product}\t{qty}\t\t{unit_price}\t\t{total_price}\n")

        file.write("-------------------------------------------------------------\n")
        file.write(f"\nYour discountable amount: {f_amount}₹")
        file.write(f"\nYour {disc}% discounted amount is: {dis}₹")
        file.write(f"\nYour payable amount is: {total}₹")
        file.write("\n\nThank You for shopping. See you again!")
        file.write("\n=============================================================\n")

    return q