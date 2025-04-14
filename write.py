def over_write(List, Dictionary):
    L = List
    d = Dictionary

    # Convert product list to a lookup dict for easier matching
    product_lookup = {item[0].upper(): i for i, item in enumerate(L)}

    for product_name in d.keys():
        product_key = product_name.upper()
        if product_key in product_lookup:
            index = product_lookup[product_key]
            L[index][2] = str(int(L[index][2]) - d[product_name])
        else:
            print(f"Warning: Product '{product_name}' not found in stock list.")

    print("\nRemaining Stock Products:\n", L)

    with open("products.txt", "w") as files:
        for each in L:
            files.write(",".join(each) + "\n")
